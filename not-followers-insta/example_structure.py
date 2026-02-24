#!/usr/bin/env python3
"""
Exemplo de como os dados exportados do Instagram podem parecer.
Use este arquivo como referência para entender a estrutura.
"""

# Exemplo de followers_1.json ou followers.json
followers_example = [
    {
        "string_list_data": [
            {
                "href": "https://www.instagram.com/usuario1",
                "value": "usuario1",
                "timestamp": 1234567890
            }
        ]
    },
    {
        "string_list_data": [
            {
                "href": "https://www.instagram.com/usuario2",
                "value": "usuario2",
                "timestamp": 1234567891
            }
        ]
    }
]

# Exemplo de following.json
following_example = {
    "relationships_following": [
        {
            "string_list_data": [
                {
                    "href": "https://www.instagram.com/usuario3",
                    "value": "usuario3",
                    "timestamp": 1234567892
                }
            ]
        },
        {
            "string_list_data": [
                {
                    "href": "https://www.instagram.com/usuario1",
                    "value": "usuario1",
                    "timestamp": 1234567893
                }
            ]
        }
    ]
}

# Neste exemplo:
# - usuario1 te segue E você segue de volta (mútuo)
# - usuario2 te segue mas você NÃO segue de volta
# - usuario3 você segue mas NÃO te segue de volta

print("📋 Estrutura de exemplo dos arquivos JSON do Instagram")
print("\nEste é apenas um exemplo. Seus arquivos reais podem ter")
print("estruturas ligeiramente diferentes, mas o script consegue")
print("lidar com múltiplos formatos.")

