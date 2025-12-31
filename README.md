# 📦 Sistema de Gestão de Estoque Farmacêutico

> Projeto desenvolvido com foco em controle de validade e rastreabilidade de lotes para a indústria farmacêutica.

## 🎯 O Problema
Em ambientes hospitalares e industriais, o controle rigoroso de insumos é vital. O desperdício por vencimento de validade e a falta de rastreabilidade de lotes geram prejuízos milionários e riscos à segurança.

## 💡 A Solução
Desenvolvi um sistema web capaz de:
- **Monitorar Validade:** Alertas visuais automáticos para produtos vencidos ou próximos do vencimento.
- **Rastrear Lotes:** Busca rápida por número de lote para recall ou conferência.
- **Prevenir Rupturas:** Alerta de estoque baixo baseado no consumo mínimo definido.

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python 3.12 + Django 5.0
- **Frontend:** HTML5, CSS3 (Bootstrap 5) e Django Templates (Jinja2)
- **Banco de Dados:** SQLite (Portável para dev) / PostgreSQL (Produção)
- **Arquitetura:** MVC (Model-View-Controller)

## 🚀 Funcionalidades
- [x] Cadastro de Produtos com Lote e Validade
- [x] Dashboard com indicadores visuais (Badges de Status)
- [x] Sistema de Busca Inteligente (Nome ou Lote)
- [x] Painel Administrativo Seguro (Django Admin)
- [x] Filtros por Categoria (Medicamentos, EPIs, Insumos)

## 📸 Screenshots
<img width="1919" height="593" alt="image" src="https://github.com/user-attachments/assets/c5170596-6ca1-40c2-beb5-8ec0b9fa6427" />

<img width="1543" height="579" alt="image" src="https://github.com/user-attachments/assets/579bd804-9418-4e0e-a0a2-f1463986e2ea" />

<img width="1520" height="794" alt="image" src="https://github.com/user-attachments/assets/2d113e30-4262-44fb-ad66-4a4503280346" />




## ⚙️ Como Rodar o Projeto

# Clone o repositório
git clone [https://github.com/icarodev10/gestao-estoque.git](https://github.com/icarodev10/gestao-estoque.git)

# Entre na pasta
cd gestao-estoque

# Crie um ambiente virtual (Opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install django

# Prepare o banco de dados
python manage.py migrate

# Crie um superusuário (para acessar o admin)
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
