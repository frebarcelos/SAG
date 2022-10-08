from personagem import personagem
from resposta import resposta
from dados import dados
from arvoreDecisao import arvoreDecisao

personagem = personagem("Frederico")
personagem.addPontosSanidade(30)
personagem.addEdu(18)
personagem.subPontosSanidade(dados.testeDehabilidade(personagem.edu))