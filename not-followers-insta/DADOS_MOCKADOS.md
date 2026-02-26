# 🔒 Dados Mockados - Instagram Non-Followers Checker

Este documento descreve as alterações feitas para remover todos os dados reais e substituí-los por dados fictícios.

## 📝 Alterações Realizadas

### 1. Arquivos de Dados Substituídos

#### `data/followers_1.json`
- **Antes:** ~1125 seguidores reais
- **Depois:** 15 seguidores fictícios com nomes genéricos
- **Formato:** Mantido o formato original do Instagram

**Seguidores mockados:**
- alice_wonder, bob_builder, charlie_photos, diana_travels, emma_art
- frank_fitness, grace_gaming, henry_hobbies, iris_inspiration, jack_jokes
- katie_kitchen, leo_lifestyle, mia_music, noah_nature, olivia_outfits

#### `data/following.json`
- **Antes:** ~1020 perfis seguidos reais
- **Depois:** 10 perfis seguidos fictícios
- **Formato:** Mantido o formato original do Instagram com `relationships_following`

**Perfis seguidos mockados:**
- alice_wonder, bob_builder, charlie_photos, diana_travels, emma_art
- paul_programmer, quinn_quotes, ryan_racing, sara_sports, tom_tech

### 2. Arquivos Removidos

Os seguintes arquivos com dados reais foram removidos:
- ❌ `non_followers_20260225_221152.txt`
- ❌ `non_followers_20260225_221411.txt`
- ❌ Todos os outros arquivos de resultado `non_followers_*.txt`

### 3. Documentação Atualizada

#### `data/README.txt`
- Atualizado para explicar a estrutura dos dados mockados
- Adicionadas instruções sobre como usar dados próprios
- Listados os resultados esperados com os dados de exemplo

## 🎯 Resultados com Dados Mockados

Ao executar o script com os dados mockados, os resultados esperados são:

```
👥 Total de seguidores: 15
👤 Total que você segue: 10
🤝 Seguidores mútuos: 5
❌ Você segue mas não te seguem: 5
➕ Te seguem mas você não segue: 10
```

### Detalhamento:

**Seguidores mútuos (5):**
- alice_wonder, bob_builder, charlie_photos, diana_travels, emma_art

**Você segue mas não te seguem (5):**
- paul_programmer, quinn_quotes, ryan_racing, sara_sports, tom_tech

**Te seguem mas você não segue (10):**
- frank_fitness, grace_gaming, henry_hobbies, iris_inspiration, jack_jokes
- katie_kitchen, leo_lifestyle, mia_music, noah_nature, olivia_outfits

## ✅ Verificação de Privacidade

- ✅ Nenhum username real permanece nos arquivos JSON
- ✅ Nenhum link real do Instagram está presente
- ✅ Timestamps foram alterados para valores genéricos
- ✅ Arquivos de resultados com dados reais foram removidos
- ✅ Todos os dados agora são completamente fictícios

## 🔧 Como Usar com Seus Próprios Dados

Para usar o script com seus dados reais do Instagram:

1. Exporte seus dados do Instagram (Configurações > Segurança > Baixar dados)
2. Aguarde o email com o link de download (pode levar até 48h)
3. Extraia o arquivo ZIP recebido
4. Substitua os arquivos em `data/`:
   - `followers_1.json` (ou `followers.json`)
   - `following.json`
5. Execute o script: `py check_followers.py`

## 📊 Benefícios dos Dados Mockados

- ✅ Permite testar o script sem expor dados pessoais
- ✅ Facilita demonstrações e compartilhamento do projeto
- ✅ Serve como exemplo da estrutura esperada dos arquivos
- ✅ Possibilita versionamento no Git sem preocupações de privacidade

