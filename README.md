# Sistemas Embarcados

**Disciplina:** Sistemas Embarcados
**Instituição:** UNIC - Universidade de Cuiabá  
**Período:** 2025/2  
**Curso:** Ciências da Computação

## 📋 Sobre a Disciplina

Esta disciplina tem como objetivo introduzir os estudantes aos conceitos fundamentais de Sistemas Embarcados, abordando a interseção entre hardware e software. Os alunos aprenderão a projetar, programar e depurar sistemas microcontrolados para aplicações do mundo real, fornecendo uma base sólida em teoria e prática.


## 📚 Pré-requisitos

    Conhecimentos sólidos de programação (C/C++ recomendado).

    Lógica de programação e estruturas de dados.

    Fundamentos de arquitetura de computadores.

    Noções de eletrônica básica (tensão, corrente, resistência, LEDs, botões).

🛠️ Tecnologias Utilizadas

## Linguagens de Programação

    C/C++ (principal)

    Python (para MicroPython/CircuitPython e scripts de automação)

    Assembly (conceitual)

## Plataformas de Hardware

    Arduino (Uno, Nano) - Plataforma de prototipagem didática.

    ESP32 / ESP8266 - Microcontroladores com Wi-Fi e Bluetooth.

    Raspberry Pi Pico (RP2040) - Microcontrolador de alta performance.

    STM32 - Família de microcontroladores padrão da indústria.

## Ferramentas de Desenvolvimento e Simulação

    Arduino IDE - Ambiente de desenvolvimento simplificado.

    PlatformIO com VS Code - Ambiente de desenvolvimento profissional.

    Tinkercad / Wokwi - Simuladores online de circuitos e microcontroladores.

    Git/GitHub - Controle de versão.

    Fritzing - Ferramenta para desenhar diagramas de circuito.

## 📁 Estrutura do Repositório

sistemas-embarcados/

└── README.md

## 🚀 Como Começar

### 1. Configuração do Ambiente

A configuração depende da plataforma de hardware escolhida. As mais comuns são:

    Para Arduino:

        Baixe e instale a Arduino IDE.

        Instale os drivers necessários para sua placa (se preciso).

        Conecte a placa, selecione o modelo e a porta COM no menu "Ferramentas".

    Para ESP32/Outras com PlatformIO:

        Instale o Visual Studio Code.

        Na aba de Extensões, procure e instale o PlatformIO IDE.

        Abra um projeto do repositório com File > Open Folder....

        O PlatformIO irá instalar as dependências (toolchains, frameworks) automaticamente.

2. Clonando o Repositório

Bash

# Clone este repositório
git clone https://github.com/seu-usuario/sistemas-embarcados.git

# Acesse o diretório de um laboratório
cd sistemas-embarcados/laboratorios/lab01-gpio-blink

3. Primeiro Projeto

    Abra o diretório do projeto na sua IDE (Arduino IDE ou VS Code com PlatformIO).

    Monte o circuito conforme especificado no README.md do laboratório.

    Carregue (upload) o código para o microcontrolador.

    Observe o resultado e experimente fazer modificações!

## 🔗 Recursos Úteis

### Documentação Oficial

    Arduino Reference

    ESP-IDF Programming Guide (para ESP32)

    Raspberry Pi Pico Datasheet

### Tutoriais e Comunidades

    Random Nerd Tutorials (excelente para ESP32 e Arduino)

    Adafruit Learning System

    SparkFun Learn

    All About Circuits

### Livros de Referência

    "Making Embedded Systems: Design Patterns for Great Code" - Elecia White

    "Embedded Systems with ARM Cortex-M Microcontrollers in Assembly Language and C" - Yifeng Zhu

    "A Linguagem de Programação C" - Kernighan & Ritchie

## 🤝 Como Contribuir

### Para Estudantes

    Faça um fork do repositório.

    Crie uma branch para sua atividade (git checkout -b lab-01-nome-sobrenome).

    Adicione seu código, esquemáticos e documentação.

    Faça commit das suas alterações (git commit -m 'Finaliza atividade do lab 01').

    Faça push para a sua branch (git push origin lab-01-nome-sobrenome).

    Abra um Pull Request para revisão.

### Padrões de Código

    Use nomes de variáveis e funções claros (ex: readTemperatureSensor() em vez de rts()).

    Comente partes complexas do código e a configuração de pinos.

    Mantenha um estilo de código consistente (indentação, chaves, etc.).

    Documente o hardware utilizado e as conexões no início do arquivo ou em um README.

### Padrões de Commit

    feat: para novas funcionalidades (ex: implementação de um novo sensor).

    fix: para correções de bugs no código.

    docs: para alterações na documentação.

    hw: para alterações em esquemáticos ou hardware.

    refactor: para refatoração de código sem alterar a funcionalidade.

    lab: para entrega de atividades de laboratório.

## 📄 Licença

Este material é destinado exclusivamente para fins educacionais da disciplina de Sistemas Embarcados do curso de Ciências da Computação da UNIC.
