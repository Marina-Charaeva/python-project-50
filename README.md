### Hexlet tests and linter status:
[![Actions Status](https://github.com/Marina-Charaeva/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Marina-Charaeva/python-project-50/actions)

### Python CI
[![Python CI](https://github.com/Marina-Charaeva/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Marina-Charaeva/python-project-50/actions/workflows/pyci.yml)

## Code Quality

[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Marina-Charaeva_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Marina-Charaeva_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Marina-Charaeva_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Marina-Charaeva_python-project-50)

### Демонстрация работы программы:
[![asciicast](https://asciinema.org/a/XHAlGhutxQL3Y96q9Zg4605Lm.svg)](https://asciinema.org/a/XHAlGhutxQL3Y96q9Zg4605Lm)
[![asciicast](https://asciinema.org/a/a5rtYq02naf7cTPbpKsmH4z9y.svg)](https://asciinema.org/a/a5rtYq02naf7cTPbpKsmH4z9y)
[![asciicast](https://asciinema.org/a/sZSPrcT5CLwmUhwkhXT85XfPr.svg)](https://asciinema.org/a/sZSPrcT5CLwmUhwkhXT85XfPr)

## Пример работы

Сравнение YAML файлов:

```bash
gendiff file1.yml file2.yml
```

Вывод:
```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

