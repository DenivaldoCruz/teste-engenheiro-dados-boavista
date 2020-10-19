#Teste de Engenharia de Dados

##Solução de ingestão de dados no Data Lake AWS

###Desafio:
- (1) Fazer a modelagem conceitual dos dados, 
- (2) Criar a infraestrutura necessária e 
- (3) criar todos os artefatos necessários para carregar os arquivos para o banco criado. 

####Arquivos a serem carregados:
    comp_boss.csv
    bill_of_materials.csv
    price_quote.csv
    
###Solução:
####Arquitetura
Stack: Amazon S3 -> AWS Glue -> AWS Athena -> Amazon Quicksight

####Implementação

#####Ingestão de dados no S3 Bucket

A ingestão dos dados pode ser feita executando o script Python upload_files_to_aws.py ou via console AWS.

Pasta do arquivo comp_boss.csv:
https://s3.console.aws.amazon.com/s3/buckets/teste-engenheiro-dados-boavista/comp-boss?region=us-east-1

Pasta do arquivo bill_of_materials.csv:
https://s3.console.aws.amazon.com/s3/buckets/teste-engenheiro-dados-boavista/bill-of-materials?region=us-east-1

Pasta do arquivo price_quote.csv:
https://s3.console.aws.amazon.com/s3/buckets/teste-engenheiro-dados-boavista/price-quote?region=us-east-1

##### Esquema de metadados no AWS Glue
https://console.aws.amazon.com/glue/home?region=us-east-1#database:name=teste-engenheiro-dados-boavista

##### Consulta dos dados ingeridos no AWS Athena
https://console.aws.amazon.com/athena/home?region=us-east-1

##### Dashboard no Amazon QuickSight para a visualização (relatório) doss dados ingeridos 
URL: https://us-east-1.quicksight.aws.amazon.com/sn/start/dashboards
Nome da conta do QuickSight: teste-engenheiro-dados-boavista
Nome do usuário: teste-engenheiro-dados-boavista