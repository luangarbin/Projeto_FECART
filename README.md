# Projeto_FECART
#descrição: #Este projeto consiste em um sistema que utiliza técnicas de visão computacional para reconhecer sinais de LIBRAS e, a partir disso, liberar uma senha para acesso para uma apresentação. O sistema foi desenvolvido em Python e faz uso de bibliotecas avançadas como OpenCV, MediaPipe e Keras.

Funcionalidades Principais: Captura de Imagem em Tempo Real: O sistema abre a câmera do dispositivo para capturar continuamente o vídeo, permitindo o reconhecimento dos sinais realizados pelo usuário.

Reconhecimento de Mãos: Utilizando a biblioteca MediaPipe, o projeto identifica e rastreia a posição das mãos em tempo real. Isso é essencial para a interpretação dos sinais de LIBRAS.

Modelo de Aprendizado de Máquina: Um modelo previamente treinado foi carregado para classificar os sinais reconhecidos. Este modelo foi desenvolvido utilizando a plataforma Teachable Machine, onde foram coletadas imagens dos sinais correspondentes às letras do alfabeto em LIBRAS.

Sistema de Autenticação por Senha: O projeto possui uma senha predefinida (neste caso, "ABCDEF") que é composta por letras que devem ser reconhecidas na sequência correta. O sistema fornece feedback ao usuário sobre o progresso da autenticação.

Interface Visual: O feedback é apresentado diretamente na tela com mensagens informativas que orientam o usuário durante o processo de reconhecimento.

Fluxo de Funcionamento: A câmera é ativada e a imagem capturada é processada para identificar as mãos. A região das mãos é isolada e normalizada para ser enviada ao modelo de reconhecimento. O modelo retorna a letra correspondente ao sinal realizado. O sistema verifica se a letra reconhecida corresponde à próxima letra da senha. Se correto, avança para a próxima letra; caso contrário, informa o usuário para tentar novamente. Quando a senha completa é reconhecida, uma mensagem de sucesso é exibida na tela. Tecnologias Utilizadas: Python: Linguagem de programação principal utilizada para o desenvolvimento do sistema. OpenCV: Biblioteca para processamento de imagem e vídeo, usada para capturar e manipular a entrada da câmera. MediaPipe: Biblioteca para reconhecimento de mãos, que facilita a detecção e rastreamento em tempo real. Keras: Utilizada para carregar e executar o modelo de aprendizado de máquina que classifica os sinais de LIBRAS. Código de Exemplo: O código em Python realiza a configuração do ambiente, a captura de vídeo, o reconhecimento de sinais e a verificação da senha. Ele inclui manipulação de exceções para garantir um feedback contínuo para o usuário.

#versao do python: 3.12.6 #bibliotecas: cv2, mediapipe, keras.models - load_model, numpy, h5py, time, threading #material: computado, camera, e suas mãos. #para funcionar: baixe todas as bibliotecas, libere a camera. #para funcionar tive pesquisar todas as biblotecas, além de ir atrás de um codigo de um user do github que corrigia um problema com a biblioteca do keras_models, e a solução foi usar mais uma biblioteca, a h5py, assim funcionando tudo
