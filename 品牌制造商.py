#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyrihgt (c) 2017 Oliver Lau
import random

def 创建随机品牌(音节数: int, 允许重复: bool = True) -> str:
  音节列表 = [
    'an',
    'be', 'ben', 'beni', 'beno', 'bi', 'best',
    'ceva', 'cos', 'cow',
    'di', 'ding', 'do', 'dong',
    'ea', 'ee', 'er', 'es', 'ë',
    'fit', 'fid', 'fow', 'fy',
    'ger', 'go',
    'hal', 'health', 'hi',
    'ke', 'ken', 'ki', 'kip', 'ku',
    'ler', 'life', 'lo', 'lz',
    'mi', 'mo', 'mr', 'mroo',
    'od', 'ok', 'oo',
    'phy', 'play', 'plus', 'por', 'pot', 'pro',
    'qi', 'qiu',
    'rap', 'rui',
    'so',
    'ta', 'tor',
    'us',
    'vi', 'vita',
    'way', 'wen',
    'xue',
    'yi', 'yo', 'you',
    'zho', 'zu'
  ]
  结果 = ''
  for _ in range(音节数):
    if len(音节列表) == 0:
      break
    s = random.choice(音节列表)
    if not 允许重复:
      音节列表.remove(s)
    结果 += s
  return 结果

for i in range(100):
  音节数 = random.randint(2, 3)
  允许重复 = random.choice([True, False])
  牌 = 创建随机品牌(音节数, 允许重复)
  print(牌, end=' ')
print()
