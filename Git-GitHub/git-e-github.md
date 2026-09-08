# Git e GitHub (DIO.me)

# O que é Git e GitHub e como eles se relacionam

Git é um sistema de controle de versão, enquanto GitHub é uma plataforma que utiliza o Git para fornecer serviços adicionais, facilitando a colaboração e o gerenciamento de projetos.

## Introdução ao Git e GitHub:

## Git:

Git é um sistema de controle de versão distribuído (DVCS), projetado para lidar eficientemente com projetos de qualquer tamanho. Ele foi desenvolvido por Linus Torvalds em 2005 para gerenciar o desenvolvimento do Kernel do Linux. O Git permite que várias pessoas trabalhem em um projeto simultaneamente, rastreando as mudanças em cada parte do código ao longo do tempo.

Em termos simples, o Git permite que você mantenha um histórico de alterações em seu código, facilitando a colaboração em equipe e o gerenciamento de projetos. Cada contribuição é registrada como um “commit”, que contém uma descrição da alteração e uma referência única (hash).

## GitHub:

GitHub, por outro lado, é uma plataforma de hospedagem de código que utiliza o Git. Fundado em 2008, o GitHub fornece um ambiente colaborativo para desenvolvedores trabalharem em projetos, facilitando o compartilhamento, colaboração e controle de versão. É especialmente popular devido à sua interface amigável e a uma série de recursos que vão além do controle de versão.

## Como eles se relacionam:

1. **Hospedagem de repositório:**
    - Git é o sistema que rastreia as alterações e gerencia o controle de versão localmente em uma máquina.
    - GitHub é um serviço que hospeda repositórios Git remotamente, permitindo que você armazene e compartilhe seu código na nuvem.
2. **Colaboração em equipe:**
    - Git possibilita a colaboração em equipe, permitindo que vários desenvolvedores trabalhem no mesmo projeto e combinem suas alterações.
    - GitHub facilita a colaboração ao fornecer recursos como “pull requests”, que permitem revisar, discutir e mesclar alterações propostas por outros membros da mesma equipe.
3. **Rastreamento de Problemas e Projetos:**
    - GitHub oferece ferramentas para rastreamento de problemas, gerenciamento de projetos e integração contínua, indo além do controle de versão.
    - Git é focado principalmente no controle de versão, enquanto o GitHub adiciona funcionalidades extras para melhorar a colaboração e o gerenciamento de projetos.
4. **Forks e Branches:**
    - Git permite criar “branches” para isolar o desenvolvimento de novos recursos ou correções de bugs.
    - GitHub estende essa funcionalidade permitindo “forks”, que são cópias independentes de um repositório, permitindo que desenvolvedores contribuam para um projeto sem modificar diretamente o repositório original.
5. **Versionamento de Código:**
    - Git controla versões localmente e realiza operações como commit, branch, e merge.
    - GitHub torna esse processo mais acessível e visível, fornecendo uma interface gráfica para navegar pelas versões, comparar alterações e colaborar de maneira eficiente.

## Configurando o Git

A configuração inicial do Git é simples, basta digitar:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "Seu E-mail"
```

## Principais Comandos do Git

1. **git init**
    - Inicia um novo repositório Git no diretório atual.
2. **git clone [URL]**
    - Clona um repositório Git existente para um diretório local.
3. **git add .**
    - Adiciona alterações ao índice (staging area) para prepará-las para o commit.
4. **git commit -m “mensagem”**
    - Realiza um commit com as alterações adicionadas, incluindo uma mensagem que descreve as mudanças feitas.
5. **git status**
    - Exibe o estado atual do repositório, indicando quais arquivos foram modificados, adicionados ou removidos.
6. **git log**
    - Mostra o histórico de commits do repositório.
7. **git branch**
    - Lista todas as branches locais e destaca a branch atual.
8. **git branch [nome-da-branch]**
    - Cria uma nova branch.
9. **git checkout [nome-da-branch]**
    - Altera para uma branch específica.
10. **git merge [branch]**
    - Combina as alterações de uma branch para a branch atual.
11. **git pull**
    - Atualiza o repositório local com as alterações do repositório remoto.
12. **git push [remote] [branch]** 
    - Envia os commits locais para o repositório remoto.
13. **git remote -v**
    - Lista os repositórios remotos configurados.
14. **git fetch**
    - Recupera as últimas alterações do repositório remoto, mas não faz merge automaticamente.
15. **git reset [arquivo]**
    - Desfaz as alterações no arquivo especificado, removendo-o do índice.
16. **git rm [arquivo]**
    - Remove um arquivo do repositório e o inclui no próximo commit.
17. **git diff**
    - Mostra as diferenças entre as alterações que ainda não foram adicionadas ao índice.
18. **git remote add [nome-remoto] [URL]**
    - Adiciona um repositório remoto com um nome específico.
19. **git push add origin main**
    - Executado para efetuar push das alterações locais para o repositório online.

# Autenticações do GitHub

## Nome de usuário e senha

Existem diferentes maneiras de se autenticar no GitHub. Uma delas é usando nome de usuário e senha, mas essa opção é considerada arriscada para informações sensíveis. Recomenda-se explorar outras opções mais seguras disponíveis.

## Token de acesso pessoal

Os PATs (Personal Access Token) são como senhas especiais que substituem o uso da senha normal ao acessar o GitHub pela API ou pela linha de comando. Você cria esse token nas configurações do GitHub e decide quais ações ele pode realizar em um repositório ou organização. Quando você usa a linha de comando do Git para trabalhar no GitHub, em vez de digitar seu nome de usuário e senha, você insere esse token para se autenticar. Isso torna a interação mais segura e prática.

## Chaves SSH

Chaves SSH são como chaves especiais que ajudam as pessoas a se conectarem a computadores remotos de forma segura, sem precisar sempre digitar senha ou token.

Ao configurar o SSH, as pessoas criam uma chave especial e a adicionam ao seu perfil no GitHub. Essa chave é protegida por uma “frase secreta” para garantir ainda mais segurança. Elas podem configurar seu computador para usar essa chave automaticamente, ou digitar a “frase secreta” quando necessário.

É possível até usar essas chaves em organizações que usam uma forma avançada de login. Se a organização fornece certificados especiais, as pessoas podem usá-los para acessar os repositórios sem precisar adicionar nada à sua conta no GitHub. Resumindo, as chaves SSH tornam as interações com o GitHub mais seguras e convenientes.

## Chaves de Implementação

Chaves de implementação são como chaves especiais que permitem acesso a apenas um lugar específico no GitHub, como um cofre digital. No GitHub, a parte da chave que todos podem ver é conectada diretamente ao local desejado (um repositório), enquanto a parte secreta fica guardada no seu próprio computador.

Essas chaves são configuradas para permitir apenas leitura por padrão, o que significa que você pode ver o que está dentro, mas não modificar nada. No entanto, se quiser também fazer alterações, você pode configurar essas chaves para ter permissão de escrita, adicionando-as ao local específico (repositório). Resumindo, são como chaves digitais que abrem a porta para u lugar específico no GitHub, e você decide se só quer olhar ou também mexer nas coisas.

## Opções de segurança adicionais

## Autenticação de dois fatores - 2FA

A autenticação de dois fatores é como adicionar uma camada extra de segurança quando você entra em sites ou aplicativos. Além de digitar seu nome de usuário e senha, você precisa fornecer mais uma prova de que é realmente você.

No caso do GitHub, essa prova extra geralmente é um código gerado por um aplicativo no seu celular ou enviado por mensagem de texto. Depois de ativar a 2FA, sempre que alguém tenta entrar na sua conta, o GitHub pede esse código adicional. Ou seja, para entrar, a pessoa precisa não só da senha, mas também do código enviado para o celular.

Os donos de organizações no GitHub podem pedir que todos, membros ou colaboradores, ativem a 2FA em suas contas pessoais. Isso dificulta para pessoas mal-intencionadas acessarem informações importantes.

Além disso, em empresas, os donos podem impor regras de segurança para todas as organizações vinculadas a uma conta corporativa, garantindo uma proteção adicional para todos os envolvidos. Resumindo, é uma maneira de deixar as coisas mais seguras na internet.

## SSO do SAML

SSO do SAML é uma forma de segurança no GitHub que permite controlar o acesso aos recursos da organização de maneira centralizada. Em vez de usar senhas, os usuários são redirecionados para um sistema central de login (IdP), como o Microsoft Entra ID ou Okta. Após autenticados, eles retornam ao GitHub com acesso aos recursos da organização.

Essa abordagem facilita o gerenciamento pois, os proprietários da organização controlam que pode acessar e o quê pode acessar. O GitHub suporta vários provedores populares como, Active Directory, Microsoft Entra Id e Okta. Em resumo, é uma maneira mais segura e eficiente de gerenciar o acesso aos dados no GitHub.

## LDAP

O LDAP é um protocolo usado para acessar e organizar informações em diretórios, especialmente em grandes empresas. No contexto do GitHub Enterprise Server, ele permite integrar e gerenciar centralmente o acesso aos repositórios usando contas existentes.

O GitHub Enterprise Server é compatível com vários serviços LDAP conhecidos como, Active Directory, Oracle Directory Server Enterprise Edition, OpenLDAP e outros. Em resumo, o LDAP é uma ferramenta que ajuda na organização e controle de acesso em ambientes corporativos no GitHub.

# Tokens de Acesso Pessoal

O token de acesso pessoal do GitHub é uma ferramenta de autenticação usada para acessar recursos e realizar ações na plataforma do GitHub em nome de um usuário.

## Passo a passo - Prático:

### Passo 1: Crie um Token de Acesso Pessoal

1. Acesse o GitHub e vá para “Settings” (Configurações) do seu perfil.
2. No menu lateral, selecione “Developer settings” (Configurações do desenvolvedor).
3. Clique em “Personal access tokens” (Tokens de acesso pessoal) e depois em “Generate token” (Gerar token).
4. Siga as instruções para configurar as permissões necessárias e clique em “Generate token” no final.
5. Copie o token gerado.

### Passo 2: Clone um Repositório usando o Token

1. Abra o Git Bash no seu computador.
2. No terminal, use o seguinte comando para clonar um repositório usando o token:
    
    ```bash
    git clone https://SEU_TOKEN_AQUI@github.com/seu-usuario/seu-repositorio.git
    ```
    
    Substitua `SEU_TOKEN_AQUI` pelo token que você copiou e `seu-usuario/seu-repositorio.git` pelo caminho do repositório que você deseja clonar.

# Chave SSH

Chaves SSH são como chaves especiais que ajudam as pessoas a se conectarem a computadores remotos de forma segura, sem precisar sempre digitar senha ou token.

## Passo a passo - Prático:

### 1 - Verificar se você já possui uma chave SSH

Antes de gerar uma nova chave SSH, verifique se você já possui uma. No terminal, execute o seguinte comando:

```bash
ls -al ~/.ssh
```

Se você já tiver uma chave SSH, normalmente os arquivos terão nomes como `id_rsa` (chave privada) e `id_rsa.pub` (chave pública).

### 2 - Gerar uma nova chave SSH (se necessário)

Se você não tiver uma chave SSH ou desejar gerar uma nova, use o seguinte comando:

```bash
ssh-keygen -t rsa -b 4096 -C "seu_email@example.com"
```

- `-t rsa` : Especifica o tipo de chave (RSA)
- `-b 4096` : Define o número de bits na chave (4096 bits é uma boa prática para maior segurança).
- `-C “seu_email@example.com”` : Adiciona um comentário para ajudar a identificar a chave (substitua pelo seu e-mail do GitHub).

Pressione Enter para aceitar o caminho padrão do arquivo (`~/.ssh/id_rsa`) e, se desejar, configure uma senha para a chave.

### 3 - Adicionar a chave ssh ao agente SSH (opcional)

Para facilitar a gestão das chaves, você pode adicionar a chave ao agente SSH:

```bash
eval "$(ssh-agent -S)"
ssh-add ~/.ssh/id_rsa
```

# 2FA

A autenticação de dois fatores (2FA) adiciona uma camada extra de segurança ao nosso login, exigindo que a gente forneça duas formas de identificação antes de acessar a sua conta.

## Passo 1: Acesse as Configurações da Conta

1. Faça login na conta GitHub.
2. No canto superior direito, clique na sua foto de perfil e selecione “Settings” (Configurações).

## Passo 2: Acesse a seção Password and Authentication

1. No menu à esquerda, clique em “Password and Authentication” (Senha e Autenticação).

## Passo 3: Configurar a Autenticação de Dois Fatores

1. No fim da página de Senhas e Autenticações, você verá a seção “Two-factor authentication” (Autenticação de dois fatores). Clique no botão “Enable two-factor authentication” (Habilite a autenticação de dois fatores).
2. Escolha o método de autenticação que você prefere. GitHub oferece duas opções principais:
    - **SMS:** Você receberá um código de autenticação via mensagem de texto.
    - **Authentication App:** Você usará um aplicativo de autenticação (como Google Authenticator, Authy, etc.) para gerar códigos temporários.
3. Siga as instruções específicas para o método escolhido. Se optar por um aplicativo de autenticação, geralmente envolve escanear o código QR ou inserir chave manualmente.
4. Após configurar o método, você será solicitado a inserir um código de verificação para confirmar que tudo está funcionando corretamente.

## Passo 4: Armazenar o Código de Recuperação

1. Após a configuração, o GitHub geralmente fornece códigos de recuperação. Esses códigos devem ser armazenados em um local seguro, pois podem ser usados para acessar sua conta se você perder o acesso ao método de autenticação principal.

## Passo 5: Conclusão

Após concluir esses passos, sua autenticação de dois fatores estará ativada. Sempre que você fizer login no GitHub, será necessário fornecer não apenas sua senha, mas também o código de autenticação gerado pelo método escolhido.

# Colaboração com o GitHub

## Antes de tudo, o que é um repositório?

Um repositório é o local onde contém todos os arquivos do nosso projeto. Seria como uma pastinha que guarda todos esses arquivos de nossos projetos, como os nossos projetos de software. É com eles que podemos colaborar, gerenciar nosso trabalho, acompanhar as alterações, armazenar o histórico de alterações, etc…

## O que são Branches?

São como uma lista de desenvolvimento separada no controle de versão. Ela permite que a gente trabalhe em modificações no código sem afetar o diretamente o código principal (geralmente chamado de branch principal, como “main” ou “master”). Isso facilita o desenvolvimento simultâneo de recursos ou correções de bugs sem interferir no código estável da versão principal. Depois de concluir as alterações em um branch, você pode mesclar essas alterações de volta ao branch principal. 

## E o Pull Request e Merge?

Um Pull Request (PR), em português significa “Solicitação de Pull” ou “Pedido de Mesclagem”. É um recurso comum em plataformas de hospedagem de código-fonte colaborativo, como o GitHub. O objetivo principal de um Pull Request é propor alterações em um repositório e solicitar que essas alterações sejam revisadas e mescladas (merged) no código principal.

Já o “Merge” é uma operação no controle de versão que combina as alterações de duas branches diferentes. Quando a gente conclui o desenvolvimento em uma branch e deseja incorporar essas alterações de volta à branch principal (ou outra branch desejada), realizamos um merge.

## Já o Fork?

É basicamente uma cópia de um repositório (um projeto de software) de outra pessoa para o seu próprio espaço no GitHub. Isso permite que você faça alterações no código sem afetar o projeto original. Se você quiser contribuir de volta, pode enviar um “pull request” para que o dono do projeto original considere suas mudanças e as incorpore.

## E as Issues?

As issues são usadas para rastrear tarefas, bugs, melhorias ou qualquer discussão relacionada ao código-fonte do projeto. Elas nos fornecem um meio de comunicação e colaboração entre os membros da equipe e da comunidade. As issues podem ser abertas por qualquer pessoa, incluindo desenvolvedores do projeto e usuários externos. Servem para discussões, planejamento, atribuição de tarefas e acompanhamento do progresso.

## Wikis no GitHub:

**Propósito:** As wikis no GitHub têm como propósito fornecer uma plataforma colaborativa para documentação de projetos. Elas são espaços onde membros da comunidade podem contribuir com informações, tutoriais e detalhes sobre o projeto, facilitando a compreensão e colaboração.

### **Para que serve:**

1. **Documentação Colaborativa:** Permite que membros da comunidade contribuam para a criação e atualização da documentação do projeto.
2. **Transparência:** Torna a informação acessível a todos, promovendo transparência sobre o funcionamento do projeto.
3. **Aprimoramento Contínuo:** Facilita a melhoria contínua da documentação à medida que o projeto evolui.
4. **Acesso Rápido:** Oferece um local centralizado para informações importantes relacionadas ao projeto.

### **Passo a Passo para utilizar Wikis no GitHub:**

1. **Criar uma Wiki:**
    - Vá para o repositório no repositório no GitHub.
    - Clique na aba “Wiki”.
    - Se não existir uma Wiki, você será solicitado a criar uma.
2. **Editar conteúdo:**
    - Cada página na Wiki tem um botão “Editar”.
    - Cliquei em “Editar” para modificar o conteúdo.
    - Utilize a linguagem de marcação Markdown para formatar a página.
3. **Histórico de revisão:**
    - A Wiki mantém um histórico de revisões.
    - É possível visualizar e reverter para versões anteriores.
4. **Controle de acesso:**
    - Gerencie quem pode editar a Wiki através das configurações de permissões do repositório.

## **Gists no GitHub:**

**Propósito:** Os Gists são destinadas a serem repositórios Git pequenos e independentes, geralmente contendo um único arquivo. Eles são úteis para compartilhar pequenos trechos de código, notas, ou até mesmo scripts.

### Para que serve:

1. **Compartilhamento rápido:** Permite compartilhar rapidamente pequenos trechos de código ou informações.
2. **Colaboração simples:** Facilita a colaboração em pequenos projetos ou soluções específicas.
3. **Visualização direta:** Os Gists podem ser visualizados diretamente no navegador, sem a necessidade de clonar o repositório.

### Passo a passo para utilizar Gists no GitHub:

1. **Criar um Gist:**
    - Vá para a página inicial do GitHub.
    - Clique em “Gist” no canto superior direito.
    - Adicione seu código ou texto e forneça uma descrição.
2. **Personalização:**
    - Escolha as opções de visibilidade (público, secreto, privado).
    - Adicione um nome de arquivo e uma descrição significativa.
3. **Salvar e compartilhas:**
    - Clique em “Create Gist” para salvar.
    - O Gist terá uma URL única para compartilhar.
4. **Revisões e Forks:**
    - Assim como em repositórios, os Gists mantêm um histórico de revisões e podem ser bifurcados (forked).

## >>> Atenção <<<

Não utilizamos mais o termo “master” como nome padrão para a branch principal, pois tem sido uma prática bastante questionada em vários contextos devido à associação histórica e simbólica do termo com a escravidão. Muitas comunidades de desenvolvimento e organizações estão buscando tornar a linguagem mais inclusiva e consciente das questões sociais.

# Adicionar, Commitar e enviar arquivos para o GitHub

Um dos passos fundamentais no GitHub é o processo de adicionar, commitar e enviar os arquivos para os nossos repositórios no GitHub, abaixo podemos ver o passo a passo desses procedimentos.

1. **Inicializar um repositório Git:**
    
    Se você ainda não tem um repositório Git, inicie um novo ou clone um existente:
    
    ```bash
    # Iniciar um novo repositório
    git init
    
    # Ou
    
    # Clonar um repositório existente
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
    
2. **Adicionar arquivos ao repositório:**
    
    Adicione os arquivos que você deseja enviar para o repositório:
    
    ```bash
    # Adicionar todos os arquivos no diretório
    git add .
    
    # Ou 
    
    # Adicionar um arquivo específico
    git add nome-do-arquivo
    ```
    
3. **Commitar as mudanças:**
    
    Commite as mudanças adicionadas, fornecendo uma mensagem descritiva:
    
    ```bash
    # A mensagem do commit dever ser clara e concisa, explicando o que foi alterado.
    git commit -m "Mensagem do Commit aqui"
    ```
    
4. **Envie para o GitHub:**
    
    Se ainda não vinculou seu repositório local a um repositório remoto no GitHub, faça isso:
    
    ```bash
    git remote add origin https://github.com/seu-usuario/seu-repositorio.git
    ```
    
    Agora, envie as alterações para o GitHub:
    
    ```bash
    git push -u origin branch-name
    ```
    
    Substitua `branch-name` pelo nome da sua branch atual (geralmente é `main` ou `master`).
    
    ```markdown
    ''' 
    	system.out.println()
    '''
    ```
    

# Formatação com o Markdown

Nesta aula, descobriremos a estrutura e a sintaxe do Markdown. Também veremos recursos do GitHub-Flavored Markdown (GFM), que são extensões de sintaxe que permitem integrar recursos do GitHub.

## O que é Markdown?

Markdown é uma linguagem de marcação que oferece uma abordagem simplificada para a edição de conteúdo, protegendo os criadores de conteúdo das complexidades do HTML. Enquanto o HTML é excelente para renderizar o conteúdo exatamente como foi pretendido, ele ocupa muito espaço e pode ser difícil de trabalhar, mesmo em pequenas doses. A invenção do Markdown ofereceu um ótimo equilíbrio entre o poder do HTML para a descrição de conteúdo e a facilidade do texto simples para edição.

## Estrutura e Sintaxe do Markdown

Nesta unidade, discutiremos a estrutura e a sintaxe do Markdown. Também abordaremos recursos do GitHub-Flavored Markdown (GFM), que são extensões de sintaxe que permitem integrar recursos do GitHub ao conteúdo.

## Sintaxe

### Enfatizar Texto

A parte mais importante de qualquer comunicação no GitHub geralmente é o texto em si, mas como mostrar que algumas partes do texto são mais importantes do que outras?

Usar o itálico no texto é tão fácil quanto cercar o texto alvo com um único asterisco (*) ou um único sublinhado (_). Certifique-se apenas de fechar uma ênfase com o mesmo caractere com o qual a abriu. Esteja atento à combinação de asteriscos e sublinhados. Aqui estão alguns exemplos:

```markdown
Isso é um texto *itálico*
Isso também é texto _itálico_
```

```markdown
Isso é um texto **negrito**
Isso também é um texto __negrito__
```

Também é possível misturar as ênfases:

```markdown
_Isso é um texto **itálico e negrito**_ usando um único sublinhado para itálico e dois asteriscos para negrito
__Isso é um texto negrito e *itálico*__ usando dois sublinhados para negrito e um único asterisco para itálico
```

Para usar um asterisco literal, anteceda-o com um caractere de escape; no GFM, isso é uma barra invertida (\). Esse exemplo resulta em sublinhados e asteriscos sendo mostrados na saída:

```markdown
\_Isso é todo \*\*texto\*\* simples\_
_Isso é todo **texto** simples_
```

### Declarar Cabeçalhos

HTML fornece cabeçalhos de conteúdo como a tag `<h1>` . No Markdown, isso é suportado via símbolo #. Basta usar um # para cada nível de cabeçalho de 1 a 6.

```markdown
# Isso é um texto H1
## Isso é um texto H2
### Isso é um texto H3
#### Isso é um texto H4
##### Isso é um texto H5
###### Isso é um texto H6
```

### Criar Listas

Você pode definir listas ordenadas ou não ordenadas. Também é possível definir itens aninhados por meio de indentação.

Listas ordenadas começam com números e listas ordenadas podem usar traços (-) ou asteriscos (*).

Ordenada:

```markdown
1. Primeiro
2. Segundo
3. Terceiro
```

Não Ordenada:

```markdown
- Primeiro
	- Aninhado
- Segundo
- Terceiro
```

### Tabelas

Você pode construir tabelas usando combinações de barras verticais (|) para quebras de colunas e traços (-) para designar a linha anterior como cabeçalho.

```markdown
| Primeiro | Segundo |
| -------- | ------- |
|     1    |     2   |
|     3    |     4   |
```

### Citar Texto

Para criar um bloco de citação, usamos o caractere maior que (>).

```markdown
> Este é um texto citado.
```

Preencher as lacunas com HTML inline

Se você se deparar com um cenário HTML não suportado pelo Markdown, pode usar HTML inline.

```markdown
Aqui está uma <br/> 
quebra de linha.
```

### Trabalhar com código

Markdown fornece um comportamento padrão para trabalhar com blocos de código inline delimitados pelo caractere de crase (’). Ao decorar o texto com esse caractere, ele é renderizado como código.

```markdown
Isso é 'código'
```

Se você tiver um segmento de código abrangendo várias linhas, pode usar três crases (’’’) antes e depois para criar um bloco de código cercado.

```markdown
'''
	var primeiro = 1;
	var segundo = 2;
	var soma = primeiro + segundo;
'''
```

### Mencionar usuários e equipes

Digitar o @ seguido do nome de um usuário do GitHub, vai enviar uma notificação para esse usuário sobre o comentário, isso chama-se “@mention”, pode ser usado também para mencionar equipes dentro de uma organização.

```bash
@VictorHugoNascimento
```

### Rastrear listas de tarefas

Você pode criar uma lista de tarefas dentro de Issues ou Pull Requests. Isso pode ser útil para acompanhar o progresso das tarefas.

```bash
- [x] Primeira tarefa
- [x] Segunda tarefa
- [ ] Terceira tarefa
```

### Comandos de barra

Comandos de barra são úteis para economizar tempo e digitação para criar um Markdown complexo.

Esses comandos podem ser usados em comentários, Issues, Pull Requests ou em discussões.

| Comando | Descrição |
| --- | --- |
| /code | Insere um bloco de código Markdown e você escolhe qual linguagem escrever. |
| /details | Insere uma área de detalhes expansível e você escolhe o título e o conteúdo. |
| /saved-replies | Insere uma resposta salva e você escolhe entre as respostas salvas para sua conta de usuário. Se adicionar %cursor% na resposta salva, o comando de barra coloca o cursos nessa localização. |
| /table | Insere uma tabela Markdown e você pode selecionar a quantidade de linhas e colunas da tabela. |
| /tasklist | Insere uma lista de tabelas mas esse comando funciona só em uma descrição de Issue. |
| /template | Mostra todos os modelos no repositório e você pode escolher o modelo a ser inserido. Este modelo funciona somente para modelos de Issue ou Pull Requests.’ |
