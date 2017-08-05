
### O que eu melhoraria para PROD

* Definir as variaveis de ambiente para as definições de PROD, seguindo um pouco do conceito do 12factor.
 
    Como nesses exemplos:
    * https://github.com/jesuejunior/stone/blob/master/stone/settings.py#L19
    
    * https://github.com/jesuejunior/stone/blob/master/stone/settings.py#L100
    
* Servir arquivos estaticos com nginx ou via S3

* Usaria o PostgreSQL como banco de dados de produção

* Implementar um pouco mais de logs com informações mais relevantes dos requests e não só apenas das queries.

* Adicionar o django swagger para documentação da API

* Implementaria o django-suit para uma interface mais amigavel(aka bonitinha) do django admin

* Implementaria o pylint para buscar ainda mais *code-smell*, comecei mais não terminei

* Não consegui ententer a usabilidade de usar o header *application/javascript* na API proposta.

    No exemplo de request tem esse header "Content-Type: application/javascript",

    Meu questionamento é que não faz muito sentido usar esse header, pois seria mais utilizado para retornar um arquivo JS estilo uma CDN, ou para usar um esquema JSONP onde precisaria/executaria um callback, assim suportaria browsers mais antigos sem suporte a CORS, por exemplo.

    Outro ponto é, usar JSONP não é recomendado para outros verbos além de GET.

* Para JSON:

    *The MIME media type for JSON text is application/json. The default encoding is UTF-8. (Source: RFC 4627).*

* Para JSONP com callback:
    *application/javascript*

* Implementaria a tag de covarage, pois hoje está em 98% de cobertura.