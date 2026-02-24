# 📖 Guia Completo de Uso

## 🚀 Início Rápido

### 1. Instalação

Execute o arquivo `install.bat` para instalar as dependências:

```bash
install.bat
```

Ou manualmente:
```bash
pip install -r requirements.txt
```

### 2. Escolha o Método

#### ✅ Método Recomendado: Dados Exportados (SEGURO)

1. **Exportar dados do Instagram:**
   - Acesse: https://www.instagram.com/download/request/
   - Ou: Instagram App → Configurações → Segurança → Baixar dados
   - Escolha formato: **JSON**
   - Aguarde o email (pode levar 24-48h)

2. **Preparar os arquivos:**
   - Baixe e extraia o arquivo ZIP recebido
   - Localize os arquivos:
     - `followers_1.json` (quem te segue)
     - `following.json` (quem você segue)
   - Copie-os para a pasta `data/`

3. **Executar:**
   ```bash
   run_safe.bat
   ```
   
   Ou manualmente:
   ```bash
   python check_followers.py
   ```

#### ⚠️ Método Alternativo: Automático (ARRISCADO)

**ATENÇÃO:** Pode violar os termos de serviço do Instagram!

```bash
run_auto.bat
```

Ou manualmente:
```bash
python check_followers_auto.py
```

## 📊 Resultados

O script irá mostrar:

1. **Estatísticas gerais:**
   - Total de seguidores
   - Total que você segue
   - Seguidores mútuos
   
2. **Lista principal:**
   - ❌ Pessoas que você segue mas não te seguem de volta
   - ➕ Pessoas que te seguem mas você não segue

3. **Arquivo de saída:**
   - `non_followers_YYYYMMDD_HHMMSS.txt` - Lista detalhada

## 🔧 Solução de Problemas

### Erro: "Arquivo não encontrado"

**Causa:** Arquivos JSON não estão na pasta `data/`

**Solução:**
1. Verifique se a pasta `data/` existe
2. Certifique-se de que os arquivos estão lá:
   - `followers_1.json` ou `followers.json`
   - `following.json`

### Erro: "JSON decode error"

**Causa:** Arquivo JSON corrompido ou formato inválido

**Solução:**
1. Re-baixe os dados do Instagram
2. Extraia novamente o arquivo ZIP
3. Verifique se os arquivos não estão vazios

### Erro: "ModuleNotFoundError"

**Causa:** Dependências não instaladas

**Solução:**
```bash
pip install -r requirements.txt
```

### Método automático: "Rate limit" ou "Bloqueado"

**Causa:** Instagram detectou automação

**Solução:**
- Aguarde algumas horas/dias
- Use o método seguro (dados exportados)

## 📁 Estrutura dos Arquivos

```
not-followers-insta/
├── check_followers.py          # Script principal (SEGURO)
├── check_followers_auto.py     # Script automático (ARRISCADO)
├── requirements.txt            # Dependências Python
├── install.bat                 # Instalador Windows
├── run_safe.bat               # Executa método seguro
├── run_auto.bat               # Executa método automático
├── README.md                  # Documentação principal
├── GUIA_DE_USO.md            # Este guia
├── example_structure.py       # Exemplo de estrutura JSON
├── .gitignore                # Arquivos ignorados pelo Git
├── data/                     # Seus arquivos JSON aqui
│   └── README.txt
└── non_followers_*.txt       # Resultados gerados
```

## 🎯 Dicas

1. **Use sempre o método seguro** (dados exportados) quando possível
2. **Não compartilhe** os arquivos JSON - contêm dados sensíveis
3. **Faça backup** dos arquivos originais antes de qualquer modificação
4. **Aguarde pacientemente** - exportação pode levar até 48h
5. **Verifique o spam** - email do Instagram pode ir para lixo eletrônico

## 🔒 Segurança

- ✅ O método de dados exportados é **100% seguro**
- ✅ Nenhuma senha é armazenada
- ✅ Nenhum dado é enviado para servidores externos
- ✅ Tudo roda localmente no seu computador

## ❓ FAQ

**P: É seguro usar este script?**
R: Sim, especialmente o método de dados exportados. Ele apenas lê arquivos locais.

**P: O Instagram vai me banir?**
R: Com o método de dados exportados, NÃO. Com o método automático, há risco.

**P: Quanto tempo leva?**
R: Exportação: 24-48h. Execução do script: segundos.

**P: Preciso saber programar?**
R: Não! Basta seguir as instruções e executar os arquivos .bat

**P: Funciona no Mac/Linux?**
R: Sim! Execute os arquivos .py diretamente com Python.

**P: Os dados ficam salvos?**
R: Sim, na pasta `data/` e nos arquivos `non_followers_*.txt`

## 📞 Suporte

Se encontrar problemas:
1. Verifique este guia completo
2. Revise a seção "Solução de Problemas"
3. Certifique-se de ter Python 3.7+ instalado
4. Verifique se as dependências foram instaladas

## 🆕 Atualizações Futuras

Possíveis melhorias:
- [ ] Interface gráfica (GUI)
- [ ] Exportação para Excel/CSV
- [ ] Gráficos e estatísticas avançadas
- [ ] Análise histórica (comparar ao longo do tempo)
- [ ] Filtros por data de follow
- [ ] Detecção de contas fantasmas/bots

---

**Versão:** 1.0
**Data:** Fevereiro 2026
**Licença:** MIT

