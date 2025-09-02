class Configuracao:

  def __init__(self, tema="claro", notificacao=True, login=False, usuario_ativo=None):
    self.tema = tema
    self.notificacao = notificacao
    self.login = login
    self.usuario_ativo = usuario_ativo

  #Tema
  @property
  def tema(self):
    return self._tema
  @tema.setter
  def tema(self, valor):
    self._tema = valor

  #Notificação
  @property
  def notificacao(self):
    return self._notificacao
  @notificacao.setter
  def notificacao(self, valor):
    self._notificacao = valor

  #Login
  @property
  def login(self):
    return self._login
  @login.setter
  def login(self, valor):
    self._login = valor

  #Usuário ativo
  @property
  def usuario_ativo(self):
    return self._usuario_ativo
  @usuario_ativo.setter
  def usuario_ativo(self, valor):
    self._usuario_ativo = valor

  #Métodos
  def fazerLogin(self, usuario_nome):
    self.login = True
    self.usuario_ativo = usuario_nome
    print(f"Login realizado com sucesso. Usuário ativo: {self.usuario_ativo}")

  def fazerLogout(self):
    self.login = False
    print("Logout realizado.")
    self.usuario_ativo = None

  def alterarTema(self, novo_tema):
    self.tema = novo_tema
    print(f"Tema alterado para: {self.tema}")

  def desativarNotificacoes(self):
    self.notificacao = False
    print("Notificações desativadas.")

  def habilitarNotificacoes(self):
    self.notificacao = True
    print("Notificações habilitadas.")

  def exibirUsuarioAtivo(self):
    if self.usuario_ativo:
      print(f"Usuário ativo: {self.usuario_ativo}")
    else:
      print("Nenhum usuário ativo.")
