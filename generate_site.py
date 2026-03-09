#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Генератор статического сайта для Wave VPN
Запустите этот файл, и он создаст папку 'site' с готовым сайтом
"""

import os
import shutil
from datetime import datetime

def create_directory(path):
    """Создает директорию, если она не существует"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"✅ Создана папка: {path}")

def write_file(filepath, content):
    """Записывает содержимое в файл"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Создан файл: {filepath}")

def generate_html():
    """Генерирует HTML-код сайта"""
    return '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wave VPN | Синий океан скорости</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(145deg, #0b1a2e 0%, #0a2a44 100%);
            color: white;
            line-height: 1.6;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Навигация */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            flex-wrap: wrap;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo h1 {
            font-size: 2rem;
            background: linear-gradient(135deg, #fff, #6ec8ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Главная секция */
        .hero {
            text-align: center;
            padding: 60px 20px;
        }
        
        .hero h2 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #ffffff, #b0e0ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .hero p {
            font-size: 1.3rem;
            color: #c3dfff;
            max-width: 700px;
            margin: 0 auto 40px;
        }
        
        /* Кнопка скачивания */
        .download-btn {
            display: inline-block;
            background: #1e90ff;
            color: white;
            text-decoration: none;
            padding: 20px 60px;
            font-size: 1.8rem;
            border-radius: 60px;
            box-shadow: 0 20px 40px #0066cc;
            transition: 0.3s;
            border: 2px solid #9bcdff;
            margin: 30px 0;
        }
        
        .download-btn:hover {
            background: #3ca0ff;
            transform: scale(1.05);
            box-shadow: 0 25px 50px #1e90ff;
        }
        
        /* Тарифы */
        .pricing {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin: 60px 0;
        }
        
        .plan {
            background: rgba(8, 38, 74, 0.7);
            border: 2px solid #1e90ff;
            border-radius: 30px;
            padding: 40px 30px;
            text-align: center;
        }
        
        .plan.free {
            border-color: #3d9cff;
        }
        
        .plan.popular {
            background: #104f8a;
            transform: scale(1.05);
            box-shadow: 0 30px 50px -15px #1e90ff;
        }
        
        .price {
            font-size: 2.5rem;
            margin: 20px 0;
        }
        
        .free-badge {
            background: #00a86b;
            padding: 10px 30px;
            border-radius: 30px;
            display: inline-block;
        }
        
        .plan ul {
            list-style: none;
            margin: 30px 0;
            text-align: left;
        }
        
        .plan li {
            margin: 15px 0;
            padding-left: 30px;
            position: relative;
        }
        
        .plan li:before {
            content: "✓";
            color: #1e90ff;
            position: absolute;
            left: 0;
            font-weight: bold;
        }
        
        .plan-btn {
            background: transparent;
            border: 2px solid #1e90ff;
            color: white;
            padding: 15px 40px;
            border-radius: 30px;
            font-size: 1.2rem;
            cursor: pointer;
            width: 100%;
            transition: 0.3s;
        }
        
        .plan-btn:hover {
            background: #1e90ff;
        }
        
        /* Статистика */
        .stats {
            display: flex;
            justify-content: center;
            gap: 60px;
            margin: 60px 0;
            flex-wrap: wrap;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1e90ff;
        }
        
        /* Футер */
        .footer {
            text-align: center;
            padding: 40px 0;
            border-top: 1px solid #1f4b77;
            margin-top: 60px;
            color: #3b6b95;
        }
        
        /* Адаптивность */
        @media (max-width: 768px) {
            .hero h2 { font-size: 2.5rem; }
            .download-btn { font-size: 1.4rem; padding: 15px 40px; }
            .pricing { grid-template-columns: 1fr; }
            .plan.popular { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Навигация -->
        <nav class="navbar">
            <div class="logo">
                <h1>🌊 WAVE VPN</h1>
            </div>
            <div>
                <a href="#" style="color: white; text-decoration: none; margin: 0 15px;">О нас</a>
                <a href="#" style="color: white; text-decoration: none; margin: 0 15px;">Тарифы</a>
                <a href="#" style="color: white; text-decoration: none; margin: 0 15px;">Поддержка</a>
            </div>
        </nav>

        <!-- Hero секция -->
        <div class="hero">
            <h2>Погружение в безопасность</h2>
            <p>Молниеносный VPN с синей лагуной защиты. Безлимитный трафик, 100+ стран.</p>
            
            <!-- Центральная кнопка -->
            <a href="https://github.com/wave-vpn/wave-releases/releases/latest" 
               class="download-btn" 
               target="_blank">
                ⬇️ Скачать Wave
            </a>
            
            <!-- Статистика -->
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-number">256-бит</div>
                    <div>шифрование</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">120+</div>
                    <div>стран</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">10 Гбит/с</div>
                    <div>скорость</div>
                </div>
            </div>
        </div>

        <!-- Тарифы -->
        <h2 style="text-align: center; font-size: 2.5rem; margin: 60px 0 30px;">🌊 Наши тарифы</h2>
        
        <div class="pricing">
            <!-- Бесплатный -->
            <div class="plan free">
                <h3>🎣 Фридайв</h3>
                <div class="price"><span class="free-badge">Бесплатно</span></div>
                <ul>
                    <li>1 устройство</li>
                    <li>30 стран</li>
                    <li>Базовый приоритет</li>
                    <li>Без рекламы</li>
                    <li>Безлимитный трафик</li>
                </ul>
                <button class="plan-btn" onclick="window.open('https://github.com/kilordow/chekerr/raw/refs/heads/main/wave.exe', '_blank')">
                    Скачать бесплатно
                </button>
            </div>
            
            <!-- Популярный -->
            <div class="plan popular">
                <h3>🌊 Цунами</h3>
                <div class="price">$7.99 <small>/мес</small></div>
                <ul>
                    <li>До 5 устройств</li>
                    <li>Все 120+ стран</li>
                    <li>Максимальная скорость</li>
                    <li>Защита от DDoS</li>
                    <li>AdBlock встроенный</li>
                    <li>Поддержка 24/7</li>
                </ul>
                <button class="plan-btn" onclick="alert('Переход к оплате...')">Выбрать тариф</button>
            </div>
            
            <!-- Премиум -->
            <div class="plan">
                <h3>🐋 Бездна</h3>
                <div class="price">$12.99 <small>/мес</small></div>
                <ul>
                    <li>Безлимит устройств</li>
                    <li>Выделенный IP</li>
                    <li>Двойной VPN</li>
                    <li>Tor over VPN</li>
                    <li>Персональный менеджер</li>
                </ul>
                <button class="plan-btn" onclick="alert('Переход к оплате...')">Окунуться</button>
            </div>
        </div>
        
        <!-- Футер -->
        <div class="footer">
            <p>© 2025 Wave VPN — синий океан анонимности</p>
            <p style="margin-top: 10px;">
                <a href="#" style="color: #6ea8ff; text-decoration: none; margin: 0 10px;">Telegram</a>
                <a href="#" style="color: #6ea8ff; text-decoration: none; margin: 0 10px;">GitHub</a>
                <a href="#" style="color: #6ea8ff; text-decoration: none; margin: 0 10px;">Discord</a>
            </p>
        </div>
    </div>
</body>
</html>
'''

def generate_readme():
    """Генерирует README файл"""
    return '''# Wave VPN

🌊 Синий океан скорости и безопасности

## О проекте
Wave VPN — это современный VPN-сервис с акцентом на скорость и анонимность.

## Тарифы
- **Фридайв** — Бесплатно (1 устройство, 30 стран)
- **Цунами** — $7.99/мес (5 устройств, все страны)
- **Бездна** — $12.99/мес (безлимит устройств, выделенный IP)

## Установка
1. Скачайте приложение из [релизов](https://github.com/kilordow/chekerr/raw/refs/heads/main/wave.exe)
2. Установите на свое устройство
3. Наслаждайтесь безопасным интернетом

## Ссылки
- [Сайт](https://[ваш-логин].github.io/wave-vpn/)
- [Скачать](https://github.com/kilordow/chekerr/raw/refs/heads/main/wave.exe)
'''

def generate_github_actions():
    """Генерирует GitHub Actions workflow для автоматической публикации"""
    return '''name: Deploy to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v4
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
'''

def main():
    """Главная функция"""
    print("🌊 Wave VPN - Генератор сайта")
    print("=" * 50)
    
    # Создаем папку для сайта
    site_dir = "wave_vpn_site"
    create_directory(site_dir)
    
    # Генерируем HTML
    html_content = generate_html()
    write_file(os.path.join(site_dir, "index.html"), html_content)
    
    # Генерируем README
    readme_content = generate_readme()
    write_file(os.path.join(site_dir, "README.md"), readme_content)
    
    # Создаем папку для GitHub Actions
    actions_dir = os.path.join(site_dir, ".github", "workflows")
    create_directory(actions_dir)
    
    # Генерируем workflow
    workflow_content = generate_github_actions()
    write_file(os.path.join(actions_dir, "deploy.yml"), workflow_content)
    
    # Создаем .gitignore
    gitignore = '''# Python
__pycache__/
*.py[cod]
*.log

# System
.DS_Store
Thumbs.db
'''
    write_file(os.path.join(site_dir, ".gitignore"), gitignore)
    
    print("\n" + "=" * 50)
    print("✅ Готово! Сайт создан в папке: " + site_dir)
    print("\n📦 Что дальше?")
    print("1. Зайдите в папку: cd " + site_dir)
    print("2. Создайте репозиторий на GitHub")
    print("3. Выполните команды:")
    print("   git init")
    print("   git add .")
    print("   git commit -m 'Первый коммит'")
    print("   git remote add origin https://github.com/kilordow/chekerr/raw/refs/heads/main/wave.exe")
    print("   git push -u origin main")
    print("\n🌐 Сайт будет доступен через 2-3 минуты по адресу:")
    print("   https://github.com/kilordow/chekerr/raw/refs/heads/main/wave.exe/")
    print("=" * 50)

if __name__ == "__main__":
    main()