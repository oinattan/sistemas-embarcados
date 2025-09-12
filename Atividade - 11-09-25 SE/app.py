from flask import Flask, jsonify, request, send_from_directory, abort
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "scripts"

app = Flask(__name__, static_folder=str(BASE_DIR), static_url_path='')

# Segurança: lista somente arquivos .py dentro da pasta scripts
@app.route('/scripts', methods=['GET'])
def list_scripts():
    files = []
    if SCRIPTS_DIR.exists():
        for p in SCRIPTS_DIR.iterdir():
            if p.is_file() and p.suffix == '.py':
                files.append(p.name)
    return jsonify(sorted(files))


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/run', methods=['POST'])
def run_script():
    data = request.get_json() or {}
    script = data.get('script')
    if not script:
        return jsonify({'error': 'script is required'}), 400

    # Prevent path traversal
    script_path = (SCRIPTS_DIR / script).resolve()
    try:
        if not str(script_path).startswith(str(SCRIPTS_DIR.resolve())):
            raise Exception('Invalid script path')
    except Exception:
        return jsonify({'error': 'invalid script path'}), 400

    if not script_path.exists() or script_path.suffix != '.py':
        return jsonify({'error': 'script not found'}), 404

    # Run the script with a timeout and capture stdout/stderr.
    # Use unbuffered mode (-u) and PYTHONUNBUFFERED to avoid missing output when Python buffers
    try:
        env = os.environ.copy()
        env['PYTHONUNBUFFERED'] = '1'
        cmd = [sys.executable, '-u', str(script_path)]
        result = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=10)
        stdout = result.stdout if result.stdout is not None else ''
        stderr = result.stderr if result.stderr is not None else ''
        # If both are empty but returncode != 0, include a helpful message
        if not stdout and not stderr and result.returncode != 0:
            stderr = f'Process exited with code {result.returncode} and no output.'

        # Log outputs to server console for debugging
        app.logger.info('Executed script: %s, returncode=%s', script, result.returncode)
        if stdout:
            # Limit log size
            app.logger.info('STDOUT:\n%s', stdout[:10000])
        if stderr:
            app.logger.warning('STDERR:\n%s', stderr[:10000])

        return jsonify({
            'script': script,
            'stdout': stdout,
            'stderr': stderr,
            'returncode': result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'timeout'}), 504
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Serve the index.html and static assets
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
