# 1.1 - Comandos Git

## Comandos para configurar o Git

```bash
git config --global user.name "Nome do usuário"
git config --global user.email "E-mail do usuário"
```

## Principais comandos do Git

- Inicia um novo repositório Git no diretório atual.
    
    ```bash
    git init
    ```
    
- Clonar um repositório
    
    ```bash
    git clone URL_do_repositório
    ```
    
- Adicionar arquivos ao índice para prepará-los para o commit
    
    ```bash
    git add .
    ```
    
- Realizar o commit e adicionar uma mensagem
    
    ```bash
    git commit -m "Mensagem do commit"
    ```
    
- Verificar o status do repositório
    
    ```bash
    git status
    ```
    
- Verificar o histórico de commits de um repositório
    
    ```bash
    git log
    ```
    
- Mostrar todas as branches e indicar qual a que está em uso no momento
    
    ```bash
    git branch
    ```
    
- Criar uma nova branch
    
    ```bash
    git branch nome-da-branch
    ```
    
- Alterar qual branch vai usar
    
    ```bash
    git checkout nome-da-branch
    ```
    
- Combinar as alterações feitas em outras branches para a atual
    
    ```bash
    git merge nome-da-branch
    ```
    
- Atualizar o repositório local com as modificações feitas no repositório remoto
    
    ```bash
    git pull
    ```
    
- Enviar os commit locais para o repositório remoto
    
    ```bash
    git push [remote] [branch]
    ```
    
- Listar todos os repositórios remotos configurados
    
    ```bash
    git remote -v
    ```
    
- Recuperar as últimas alterações do repositório remoto, mas não realizar o merge automaticamente
    
    ```bash
    git fetch
    ```
    
- Desfazer as alterações de um arquivo específico e removê-lo do índice
    
    ```bash
    git reset nome-do-arquivo
    ```
    
- Remover o arquivo do repositório e incluí-lo no próximo commit
    
    ```bash
    git rm nome-do-arquivo
    ```
    
- Mostrar as diferenças entre as alterações que ainda não foram enviadas ao índice
    
    ```bash
    git diff
    ```
    
- Adicionar um repositório remoto com um nome específico
    
    ```bash
    git remote add nome-remoto url-do-repositório
    ```
    
- Enviar as alterações do repositório local para o repositório remoto
    
    ```bash
    git push add origin main
    ```