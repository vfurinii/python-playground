📂 DADOS DE EXEMPLO (MOCKADOS)
============================================================

Esta pasta contém dados fictícios de exemplo para demonstração.

ESTRUTURA DOS DADOS MOCKADOS:
------------------------------------------------------------

followers_1.json - 15 seguidores fictícios:
  • alice_wonder, bob_builder, charlie_photos, diana_travels, emma_art
  • frank_fitness, grace_gaming, henry_hobbies, iris_inspiration, jack_jokes
  • katie_kitchen, leo_lifestyle, mia_music, noah_nature, olivia_outfits

following.json - 10 perfis seguidos fictícios:
  • alice_wonder, bob_builder, charlie_photos, diana_travels, emma_art
  • paul_programmer, quinn_quotes, ryan_racing, sara_sports, tom_tech

RESULTADOS ESPERADOS:
------------------------------------------------------------
  👥 Seguidores mútuos: 5
  ❌ Seguindo mas não te seguem: 5
  ➕ Te seguem mas não segue: 10

============================================================

COMO USAR SEUS PRÓPRIOS DADOS:
------------------------------------------------------------

Para exportar seus dados reais do Instagram:
1. Acesse Instagram > Configurações > Segurança > Baixar dados
2. Escolha formato JSON
3. Aguarde o email do Instagram (pode levar até 48h)
4. Extraia os arquivos JSON e substitua os arquivos nesta pasta:
   - followers_1.json (ou followers.json)
   - following.json
