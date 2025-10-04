def build_profile(first, last, **user_info):
    """Cria um dicionário com informações sobre um perfil de usuário."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('livia', 'mello', location='campinas', course='ads')
print(user_profile)