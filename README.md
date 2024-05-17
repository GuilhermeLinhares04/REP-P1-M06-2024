# REP-P1-M06-2024

Este repositório contém um projeto em ROS 2, capaz de mover a tartaruga do **_turtesim_** utilizando uma interface por linha de comando (CLI)

## Requisitos

Para executar este projeto, é necessário ter o **ROS 2** e o **turtlesim** instalados além de possuir o **Linux** como sistema operacional (também é possível utiliar o WSL).

É necessário realizar este [tutorial](https://rmnicola.github.io/m6-ec-encontros/workspaces#12-workspace-ros) para criar seu workspace para a execução do projeto.

## Como executar

Para executar o projeto, siga os passos abaixo:

1. Clone este repositório;
2. Cole a a pasta do repositório no caminho `seu_workspace/src`, após ter realizado o tutorial de criação de workspaces
3. Abra um terminal e navegue até a pasta do seu workspace utilizando o comando `cd seu_workspace`
5. Execute o comando `colcon build`, para compilar o projeto;
6. Execute o comando `source install/setup.bash`, para carregar as variáveis de ambiente;
7. Execute o comando `ros2 run clturtle_control clturtle_node`, para executar o projeto.

## Vídeo de demonstração

Clique na imagem abaixo para assistir ao vídeo de demonstração do projeto:

[![Vídeo de demonstração](https://arminlab.com/wp-content/uploads/2022/09/icons8-youtube-play-button-2048-300x300.png)](https://youtu.be/vlLFJW5KrEY)
