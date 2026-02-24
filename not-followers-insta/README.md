# Instagram Non-Followers Checker - POC

Este é um Proof of Concept (POC) para verificar quem você segue no Instagram mas que não te segue de volta.

## Como Funcionar

### Método 1: Usando dados exportados do Instagram (Recomendado e Seguro)

1. **Exportar seus dados do Instagram:**
   - Acesse Instagram > Configurações > Segurança > Baixar dados
   - Ou use este link direto: https://www.instagram.com/download/request/
   - Escolha formato JSON
   - Aguarde o Instagram enviar o arquivo por email (pode levar até 48h)

2. **Extrair os arquivos:**
   - Descompacte o arquivo ZIP recebido
   - Localize os arquivos:
     - `followers_1.json` (quem te segue)
     - `following.json` (quem você segue)

3. **Copiar para o diretório:**
   - Coloque os arquivos JSON na pasta `data/`

4. **Executar o script:**
   ```bash
   python check_followers.py
   ```

### Método 2: Usando Instaloader (Automático, mas requer login)

```bash
python check_followers_auto.py
```

⚠️ **Aviso:** O Instagram pode detectar automação e bloquear temporariamente sua conta. Use por sua conta e risco.

## Instalação

```bash
pip install -r requirements.txt
```

## Arquivos

- `check_followers.py` - Script principal usando dados exportados (SEGURO)
- `check_followers_auto.py` - Script automático usando Instaloader (ARRISCADO)
- `requirements.txt` - Dependências Python
- `data/` - Diretório para arquivos JSON exportados

## Resultados

O script irá gerar:
- Lista de pessoas que você segue mas não te seguem de volta
- Arquivo `non_followers.txt` com os resultados
- Estatísticas sobre seus seguidores

## Segurança

✅ **Método 1 (Dados Exportados):** Completamente seguro, usa dados oficiais do Instagram
❌ **Método 2 (Automático):** Pode violar os termos de serviço do Instagram

Use o Método 1 sempre que possível!

