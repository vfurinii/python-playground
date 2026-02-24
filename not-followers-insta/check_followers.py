#!/usr/bin/env python3
"""
Instagram Non-Followers Checker - Usando dados exportados do Instagram
Este método é SEGURO e não viola os termos de serviço do Instagram.
"""

import json
import os
from pathlib import Path
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    print("Dica: Instale 'colorama' para ter saída colorida: pip install colorama")


class InstagramFollowersChecker:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.followers = set()
        self.following = set()

    def load_json_file(self, filename):
        """Carrega arquivo JSON do diretório de dados."""
        filepath = self.data_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def extract_usernames(self, data, key_path):
        """Extrai usernames de estruturas JSON variadas do Instagram."""
        usernames = set()

        # Instagram pode ter diferentes formatos de exportação
        # Tentamos vários formatos possíveis

        if isinstance(data, list):
            for item in data:
                # Formato: [{"string_list_data": [{"value": "username"}]}]
                if "string_list_data" in item:
                    for string_data in item["string_list_data"]:
                        if "value" in string_data:
                            usernames.add(string_data["value"])
                        elif "href" in string_data:
                            # Extrai username da URL
                            username = string_data["href"].split("/")[-2]
                            usernames.add(username)

                # Formato direto: [{"username": "user"}]
                elif "username" in item:
                    usernames.add(item["username"])

                # Formato: [{"value": "username"}]
                elif "value" in item:
                    usernames.add(item["value"])

        elif isinstance(data, dict):
            # Se for dict, pode ter chaves como "followers_1", "following", etc.
            for key, value in data.items():
                if isinstance(value, list):
                    usernames.update(self.extract_usernames(value, key_path))

        return usernames

    def load_followers(self):
        """Carrega lista de seguidores."""
        print("📥 Carregando lista de seguidores...")

        # Tenta diferentes nomes de arquivo possíveis
        possible_files = ["followers_1.json", "followers.json"]

        for filename in possible_files:
            try:
                data = self.load_json_file(filename)
                self.followers = self.extract_usernames(data, "followers")
                print(f"✅ {len(self.followers)} seguidores carregados de {filename}")
                return
            except FileNotFoundError:
                continue

        raise FileNotFoundError(
            "Arquivo de seguidores não encontrado. Procure por 'followers_1.json' ou 'followers.json' "
            "no arquivo ZIP exportado do Instagram."
        )

    def load_following(self):
        """Carrega lista de quem você segue."""
        print("📥 Carregando lista de quem você segue...")

        data = self.load_json_file("following.json")

        # O arquivo following.json pode ter estrutura diferente
        if isinstance(data, dict) and "relationships_following" in data:
            data = data["relationships_following"]

        self.following = self.extract_usernames(data, "following")
        print(f"✅ {len(self.following)} perfis que você segue foram carregados")

    def find_non_followers(self):
        """Encontra pessoas que você segue mas não te seguem de volta."""
        return self.following - self.followers

    def find_not_following_back(self):
        """Encontra pessoas que te seguem mas você não segue de volta."""
        return self.followers - self.following

    def print_colored(self, text, color=None):
        """Imprime texto com cor se disponível."""
        if COLORS_AVAILABLE and color:
            print(color + text + Style.RESET_ALL)
        else:
            print(text)

    def generate_report(self):
        """Gera relatório completo."""
        non_followers = self.find_non_followers()
        not_following_back = self.find_not_following_back()
        mutual_followers = self.followers & self.following

        # Cabeçalho
        self.print_colored("\n" + "="*60, Fore.CYAN if COLORS_AVAILABLE else None)
        self.print_colored("📊 RELATÓRIO DE SEGUIDORES DO INSTAGRAM", Fore.CYAN if COLORS_AVAILABLE else None)
        self.print_colored("="*60 + "\n", Fore.CYAN if COLORS_AVAILABLE else None)

        # Estatísticas
        print(f"👥 Total de seguidores: {len(self.followers)}")
        print(f"👤 Total que você segue: {len(self.following)}")
        print(f"🤝 Seguidores mútuos: {len(mutual_followers)}")
        print(f"❌ Você segue mas não te seguem: {len(non_followers)}")
        print(f"➕ Te seguem mas você não segue: {len(not_following_back)}")

        # Não te seguem de volta
        if non_followers:
            self.print_colored(f"\n{'='*60}", Fore.RED if COLORS_AVAILABLE else None)
            self.print_colored(f"❌ PESSOAS QUE VOCÊ SEGUE MAS NÃO TE SEGUEM DE VOLTA ({len(non_followers)}):",
                             Fore.RED if COLORS_AVAILABLE else None)
            self.print_colored("="*60, Fore.RED if COLORS_AVAILABLE else None)

            sorted_non_followers = sorted(non_followers)
            for i, username in enumerate(sorted_non_followers, 1):
                print(f"{i:4d}. @{username}")

            # Salva em arquivo
            output_file = f"non_followers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Pessoas que você segue mas não te seguem de volta ({len(non_followers)}):\n")
                f.write("="*60 + "\n\n")
                for username in sorted_non_followers:
                    f.write(f"@{username}\n")

            self.print_colored(f"\n💾 Lista salva em: {output_file}", Fore.GREEN if COLORS_AVAILABLE else None)

        # Você não segue de volta
        if not_following_back:
            self.print_colored(f"\n{'='*60}", Fore.YELLOW if COLORS_AVAILABLE else None)
            self.print_colored(f"➕ PESSOAS QUE TE SEGUEM MAS VOCÊ NÃO SEGUE DE VOLTA ({len(not_following_back)}):",
                             Fore.YELLOW if COLORS_AVAILABLE else None)
            self.print_colored("="*60 + "\n", Fore.YELLOW if COLORS_AVAILABLE else None)

            # Mostra apenas os primeiros 20
            sorted_not_following = sorted(not_following_back)
            for i, username in enumerate(sorted_not_following[:20], 1):
                print(f"{i:4d}. @{username}")

            if len(not_following_back) > 20:
                print(f"\n... e mais {len(not_following_back) - 20} pessoas")

        print("\n" + "="*60 + "\n")


def main():
    print("🔍 Instagram Non-Followers Checker")
    print("="*60)
    print("\nEste script analisa os dados exportados do Instagram.")
    print("\n📋 INSTRUÇÕES:")
    print("1. Exporte seus dados do Instagram (Configurações > Segurança > Baixar dados)")
    print("2. Coloque os arquivos JSON na pasta 'data/':")
    print("   - followers_1.json (ou followers.json)")
    print("   - following.json")
    print("3. Execute este script\n")
    print("="*60 + "\n")

    # Cria diretório data se não existir
    data_dir = Path("data")
    if not data_dir.exists():
        data_dir.mkdir()
        print(f"📁 Diretório '{data_dir}' criado.")
        print("   Por favor, coloque seus arquivos JSON lá e execute novamente.")
        return

    # Verifica se há arquivos JSON
    json_files = list(data_dir.glob("*.json"))
    if not json_files:
        print("⚠️  Nenhum arquivo JSON encontrado na pasta 'data/'")
        print("   Por favor, adicione seus arquivos exportados do Instagram.")
        return

    print(f"✅ Encontrados {len(json_files)} arquivos JSON na pasta 'data/'\n")

    try:
        checker = InstagramFollowersChecker()
        checker.load_followers()
        checker.load_following()
        checker.generate_report()

    except FileNotFoundError as e:
        print(f"\n❌ Erro: {e}")
        print("\n💡 Certifique-se de que você tem os seguintes arquivos na pasta 'data/':")
        print("   - followers_1.json (ou followers.json)")
        print("   - following.json")
    except json.JSONDecodeError as e:
        print(f"\n❌ Erro ao ler arquivo JSON: {e}")
        print("   Verifique se os arquivos não estão corrompidos.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

