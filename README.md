Django-Rest
O projeto Django-Rest é uma API de escola desenvolvida em Python utilizando o Django REST Framework. A api permite o gerencimento e controle de Alunos, Cursos e Matriculas. Este projeto implementa autenticação de usuários,validação de dados, documentação da API e testes automatizados.

Índice
Funcionalidades
Autenticação de Usuários
Validação de dados
Documentação da API
Testes
Como Contribuir
Licença
Instalação
Clone o repositório:


Autenticação e autorização utilizando Django REST Framework
Sistema de doações de itens
Filtragem de doações disponíveis
Documentação automatizada da API (Swagger)
Testes automatizados
Autenticação de Usuários
O sistema utiliza o Django REST Framework para autenticar usuários por meio de tokens. Para autenticação, você pode enviar suas credenciais de login para o endpoint /api/token/ e receber um token JWT.

Endpoints:
Registrar Usuário: /api/register/
Obter Token: /api/token/
Renovar Token: /api/token/refresh/
Verificar Token: /api/token/verify/
Exemplo de uso (via curl):
bash
Copiar código
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "seu-usuario", "password": "sua-senha"}'
Documentação da API
A documentação da API é gerada automaticamente utilizando o pacote drf-yasg. Você pode acessá-la nos seguintes endpoints:

Swagger UI: http://localhost:8000/swagger/
Redoc: http://localhost:8000/redoc/
Testes
O projeto inclui testes automatizados para verificar a integridade das funcionalidades. Os testes foram implementados utilizando o framework de testes do Django.

Como executar os testes:
No diretório raiz do projeto, execute o comando:

bash
Copiar código
python manage.py test
Isso executará todos os testes disponíveis para garantir que as funcionalidades estejam funcionando corretamente.

Como Contribuir
Se você deseja contribuir com o projeto, siga estas etapas:

Faça um fork do projeto.
Crie uma nova branch para suas alterações: git checkout -b minha-branch.
Commit suas mudanças: git commit -m 'Minha nova funcionalidade'.
Envie para sua branch: git push origin minha-branch.
Abra um Pull Request.
Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
