# TAREFA 1
Solicitação:
- Crie um repositorio no github e uma nova branch chamada develop mantendo a main para o projeto que for para produção. Inclua um README.md com instruções sobre. Demonstre um exemplo de como você criaria um branch de feature, faria mudanças e as mesclaria de volta ao branch principal.<br>

Resolução:
- Repositório criado https://github.com/th1alexandre/360crm-devops-test
- Possui duas branchs, main para ambiente de produção e develop para ambiente de staging
- Este é o arquivo README.md solicitado
- Criar uma nova branch de feature a partir da branch develop:
```
  git checkout develop
  git pull origin develop
  git checkout -b feature/nome-da-feature
```
- Fazer mudanças na branch de feature e commit:
```
  git add .
  git commit -m "Descrição das mudanças feitas na feature"
```
- Enviar a branch de feature para o repositório remoto:
```
  git push origin feature/nome-da-feature
```
- Criar um Pull Request (PR) no GitHub:
  - Vá até o repositório no GitHub.
  - Clique em "Pull Requests".
  - Clique em "New Pull Request".
  - Selecione a branch develop como base e a branch feature/nome-da-feature como compare.
  - Clique em "Create Pull Request".
- Revisar o código e aprovar o PR:
  - Solicitar a um colega para revisar o código.
  - O revisor deve olhar o código, fazer comentários se necessário e aprovar o PR.
- Mesclar o PR na branch develop:
  - Após a aprovação, clique em "Merge pull request" no GitHub.
  - Clique em "Confirm merge".
  - Ou utilize o terminal git para realizar o merge através dos seguintes comandos
```
  git checkout develop
  git pull origin develop
  git merge feature/nome-da-feature
  git push origin develop
```
- Explicação Breve: Pull Request e Code Review
  - Pull Request (PR): Um PR é uma solicitação para mesclar mudanças de uma branch de feature para outra branch, geralmente develop ou main. Ele permite que outros desenvolvedores revisem o código antes da mesclagem.
  - Code Review: Antes de aprovar um PR, deve ser feita uma revisão do código para garantir que ele atende aos padrões de qualidade, não introduz bugs, e segue as práticas recomendadas. Os revisores podem comentar no código, sugerir mudanças e, finalmente, aprovar o PR. Uma vez aprovado, o PR pode ser mesclado na branch alvo.
- Excluir a branch de feature (opcional, mas recomendado):
  - Na configuração do repositório no GitHub é possível marcar para deletar automaticamente a branch feature após a mesma ter sido mesclada com as branchs develop/main evitando acumulo de branchs fantasmas, também é possível excluir as branchs de feature manualmente após concluir o desenvolvimento através dos seguintes comandos em um terminal git
```
  git branch -d feature/nome-da-feature
  git push origin --delete feature/nome-da-feature
```
<br><br>
# TAREFA 2
Solicitação:
- Use o Terraform para provisionar a infraestrutura necessária para o ambiente de staging na sua máquina local, utilizando o LocalStack para simular os serviços da AWS (Criar um bucket S3, uma tabela DynamoDB).Nessa parte é esperado no repositorio do projeto os arquivos .tf utilizados para a criação dos recursos S3 e Dynamodb juntamente com os arquivos de provisionamento do LocalStack para avalidor testar.<br>

Resolução:
- Acesse a pasta `/terraform` na raiz do repositório
  - Na pasta `modules` temos os arquivos `.tf` relacionados para a criação dos recursos `aws s3` e `aws dynamoDB` bem como variáveis exigidas.
  - Voltando a pasta `/terraform` temos os arquivos `.tf` relacionados ao `provider` que no nosso caso é AWS, `main.tf` contendo os recursos a serem criados e `variables.tf` contendo as variáveis necessárias para o deploy do projeto
- Instruções sobre arquivos `.tfvars`
  - Não comitar `terraform.tfvars`: Esse arquivo não deve ser incluído no controle de versão (git) para evitar o vazamento de informações sensíveis. Por essa razão o mesmo é ignorado pelo git através de configuração no arquivo `.gitignore` do repositório
  - Arquivo de exemplo: Para auxiliar os desenvolvedores na configuração das variáveis, um arquivo de exemplo com valores pré-populados é fornecido como `terraform.tfvars.localstack`. Este arquivo serve como referência para que os desenvolvedores saibam quais variáveis precisam ser definidas e quais os formatos esperados.
- Motivo para Não Comitar arquivos `.tfvars`
  - O arquivo `terraform.tfvars` contém variáveis sensíveis e específicas do ambiente, como chaves de acesso, URLs de endpoints, credenciais e outras configurações que são cruciais para a infraestrutura. Comitar esse arquivo no repositório pode comprometer a segurança do projeto, expondo informações confidenciais que podem ser usadas para acessar ou manipular recursos da infraestrutura.
- Provisionamento do `localstack`
  - Provisionado através do arquivo `docker-compose.yml` na raíz do repositório
  - Após iniciar a aplicação via docker-compose é necessário primeiro executar os comandos do `terraform apply` para criação dos recursos AWS localmente, [link do manual para uso do terraform via localstack](https://docs.localstack.cloud/user-guide/integrations/terraform/), o script terraform irá provisionar a tabela DynamoDB que é utilizada pela aplicação para armazenamento dos logs do app python/flask
  - Após provisionar os recursos sinta-se livre para interagir com o back-end acessando o link http://localhost:5000/apidocs através de um navegador
<br><br>
# TAREFA 3
Solicitação:
- Crie um cluster do Kubernetes com Kind usando o Terraform configurando as roles para cada parte do cluster(Controlplane,ETCD, Worker...) poste no README.md os comandos utilizados para criar o cluster. <br>

Resolução:
- Provisionamento de cluster K8s utilizando [Kind](https://kind.sigs.k8s.io/) e [Terraform](https://registry.terraform.io/providers/tehcyx/kind/latest)
- Arquivos relacionados a configuração do cluster localizados em `./terraform/kind.tf` e `./terraform/provider.tf`
- Executar `tflocal apply` e o cluster será criado junto com os recursos da AWS via localstack
<br><br>
# TAREFA 4
Solicitação:
- Faça um fork desse repositorio e crie um Dockerfile para contêinerizar esta aplicação https://github.com/python019/django_crm. É esperado em seu repositorio, uma pasta com o codigo fonte do fork e Dockerfile desenvolvido para o avaliador testar. <br>

Resolução:
- Link do fork contendo o Dockerfile gerado https://github.com/th1alexandre/django_crm
- Também foi criado um arquivo `docker-compose.yml` para rápida inicialização do app
- Recomendado verificar o último commit para conferir todas as alterações que foram feitas no fork
<br><br>

<br><br><br><br>
## Configuring Your Development Environment

### Configure your SSH and GPG Keys
These steps are not required, but highly recommended
- Connect to GitHub using the [Secure Shell Protocol](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- Use [GPG Keys](https://docs.github.com/en/authentication/managing-commit-signature-verification) to configure commit signature

### Install Docker
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or...
- - [Docker Engine](https://docs.docker.com/engine/install/)
- - [Docker Compose](https://docs.docker.com/compose/install/)

### Set your environment variables
- Create a new file named `.env` in the root folder
- Copy the content of the `.env.dev` file to the new `.env`
- Update the variable values with your preferences
- - When adding new keys, remember to pass it to `docker-compose.yml` and `.env.dev`
- - This helps others developers configuring and updating their development environment

### Create Python Virtual Environment
- Download and install [Python](https://www.python.org/downloads/) with your desired version
- Run `python<version> -m venv .venv` to create a new python virtual environment
- - You can choose other names than `.venv`, just be careful to avoid conflicts with `.env` file
- - Check [this docs](https://docs.python.org/3/library/venv.html) for more info about using venv module

### Install project dependencies
- Activate your virtual environment `.venv`
- Run `pip install poetry` and `poetry install --only main`
- After installing main dependencies, install dev dependencies
- Run `poetry install --only dev` and `pre-commit install`
