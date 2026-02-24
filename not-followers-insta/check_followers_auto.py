#!/usr/bin/env python3
"""
Instagram Non-Followers Checker - Usando Instaloader (Automático)
⚠️ AVISO: Este método pode violar os termos de serviço do Instagram.
Use por sua conta e risco. O método seguro é usar check_followers.py
"""

import sys
from pathlib import Path

try:
    import instaloader
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError as e:
    print("❌ Erro: Dependências não instaladas.")
    print("Execute: pip install -r requirements.txt")
    sys.exit(1)


class InstagramAutoChecker:
    def __init__(self):
        self.loader = instaloader.Instaloader()
        self.username = None
        self.profile = None

    def login(self, username, password=None):
        """Faz login no Instagram."""
        self.username = username

        if password:
            try:
                print(f"🔐 Fazendo login como @{username}...")
                self.loader.login(username, password)
                print("✅ Login realizado com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao fazer login: {e}")
                print("\n💡 Dica: O Instagram pode bloquear logins automáticos.")
                print("   Use o método seguro: check_followers.py")
                sys.exit(1)
        else:
            # Tenta carregar sessão salva
            try:
                self.loader.load_session_from_file(username)
                print(f"✅ Sessão carregada para @{username}")
            except FileNotFoundError:
                print("❌ Nenhuma sessão encontrada.")
                print("   Execute novamente fornecendo senha.")
                sys.exit(1)

    def get_profile(self):
        """Obtém perfil do usuário."""
        print(f"📥 Carregando perfil de @{self.username}...")
        try:
            self.profile = instaloader.Profile.from_username(
                self.loader.context,
                self.username
            )
            print(f"✅ Perfil carregado: {self.profile.full_name}")
            print(f"   Seguidores: {self.profile.followers}")
            print(f"   Seguindo: {self.profile.followees}")
        except Exception as e:
            print(f"❌ Erro ao carregar perfil: {e}")
            sys.exit(1)

    def get_followers(self):
        """Obtém lista de seguidores."""
        print("\n📥 Carregando seguidores (isso pode demorar)...")
        followers = set()
        try:
            for follower in self.profile.get_followers():
                followers.add(follower.username)
                if len(followers) % 100 == 0:
                    print(f"   Carregados {len(followers)} seguidores...")
            print(f"✅ Total: {len(followers)} seguidores")
            return followers
        except Exception as e:
            print(f"❌ Erro ao carregar seguidores: {e}")
            print("   O Instagram pode ter limitado sua taxa de requisições.")
            return followers

    def get_following(self):
        """Obtém lista de quem você segue."""
        print("\n📥 Carregando lista de quem você segue (isso pode demorar)...")
        following = set()
        try:
            for followee in self.profile.get_followees():
                following.add(followee.username)
                if len(following) % 100 == 0:
                    print(f"   Carregados {len(following)} perfis...")
            print(f"✅ Total: {len(following)} perfis que você segue")
            return following
        except Exception as e:
            print(f"❌ Erro ao carregar seguindo: {e}")
            print("   O Instagram pode ter limitado sua taxa de requisições.")
            return following

    def generate_report(self, followers, following):
        """Gera relatório."""
        non_followers = following - followers
        not_following_back = followers - following
        mutual = followers & following

        print("\n" + Fore.CYAN + "="*60)
        print(Fore.CYAN + "📊 RELATÓRIO DE SEGUIDORES DO INSTAGRAM")
        print(Fore.CYAN + "="*60 + Style.RESET_ALL)

        print(f"\n👥 Total de seguidores: {len(followers)}")
        print(f"👤 Total que você segue: {len(following)}")
        print(f"🤝 Seguidores mútuos: {len(mutual)}")
        print(f"❌ Você segue mas não te seguem: {len(non_followers)}")
        print(f"➕ Te seguem mas você não segue: {len(not_following_back)}")

        if non_followers:
            print(Fore.RED + f"\n{'='*60}")
            print(Fore.RED + f"❌ NÃO TE SEGUEM DE VOLTA ({len(non_followers)}):")
            print(Fore.RED + "="*60 + Style.RESET_ALL)

            sorted_non = sorted(non_followers)
            for i, username in enumerate(sorted_non, 1):
                print(f"{i:4d}. @{username}")

            # Salva em arquivo
            output_file = "non_followers_auto.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Pessoas que você segue mas não te seguem de volta ({len(non_followers)}):\n")
                f.write("="*60 + "\n\n")
                for username in sorted_non:
                    f.write(f"@{username}\n")

            print(Fore.GREEN + f"\n💾 Lista salva em: {output_file}")

        print("\n" + "="*60 + "\n")


def main():
    print(Fore.YELLOW + "⚠️  AVISO IMPORTANTE" + Style.RESET_ALL)
    print("="*60)
    print("Este script usa automação para acessar o Instagram.")
    print("Isso pode violar os termos de serviço e resultar em:")
    print("  - Bloqueio temporário da conta")
    print("  - Limitação de taxa (rate limiting)")
    print("  - Suspensão da conta")
    print("\n💡 RECOMENDAÇÃO: Use o método seguro 'check_followers.py'")
    print("   que analisa dados exportados oficialmente do Instagram.")
    print("="*60 + "\n")

    response = input("Deseja continuar mesmo assim? (sim/não): ").strip().lower()
    if response not in ['sim', 's', 'yes', 'y']:
        print("Operação cancelada. Use 'check_followers.py' para o método seguro.")
        return

    print("\n" + "="*60)
    username = input("Digite seu username do Instagram (sem @): ").strip()

    print("\n💡 Por segurança, não armazene sua senha em texto plano.")
    print("   Você pode pressionar Enter para usar uma sessão salva.")
    password = input("Digite sua senha (ou Enter para sessão salva): ").strip()

    if not password:
        password = None

    print("\n" + "="*60 + "\n")

    checker = InstagramAutoChecker()
    checker.login(username, password)
    checker.get_profile()

    followers = checker.get_followers()
    following = checker.get_following()

    if followers and following:
        checker.generate_report(followers, following)
    else:
        print("\n❌ Não foi possível carregar os dados.")
        print("   Tente novamente mais tarde ou use o método seguro.")


if __name__ == "__main__":
    main()

