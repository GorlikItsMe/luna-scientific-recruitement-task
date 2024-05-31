# luna-scientific-recruitement-task

## How to install?

```bash
# todo
```

## How to run?

```bash
# todo
```

## Zadanie

Cel: Stworzenie prostej aplikacji CRUD w Django, która umożliwia zarządzanie
systemem hydroponicznym.

### Wymagania funkcjonalne

#### Endpoint do zarządzania systemem hydroponicznym

- [x] Umożliwić użytkownikowi tworzenie, odczytywanie, aktualizowanie, i
usuwanie (CRUD) informacji o jego systemach hydroponicznych.
- [x] Każdy system hydroponiczny powinien być przypisany do użytkownika
(owner).
- [x] Powinna zostać dodana walidacja danych zgodna z zaleceniamy
Django REST Framework.

#### Endpoint do zarządzania pomiarami

- [x] Umożliwić wysyłanie danych z czujników (pH, temperatura wody, TDS)
do istniejącego systemu hydroponicznego.
- [x] Pomiary powinny być zapisywane w bazie danych.

#### Odczytywanie informacji o systemach i pomiarach

- [x] Użytkownik powinien mieć możliwość otrzymania listy swoich
systemów hydroponicznych.
- [x] Wszelkie metody pobierania danych powinny dawać możliwość
filtrowania danych (przedział czasowy, przedział wartości).
- [x] Metody te powinny też dawać opcje sortowania wyników po wybranych
parametrach.
- [x] W metodach, gdzie będzie to potrzebne należy zaimplementować
paginację danych.
- [x] Możliwość pobrania szczegółów konkretnego systemu z informacją o
10 ostatnich pomiarach.

#### Endpoint logowania użytkownika

- [ ] System autoryzacji i uwierzytelniania użytkowników.

### Wymagania techniczne

- [x] Aplikacja powinna być napisana w Django z wykorzystaniem Django REST
Framework.
- [x] Użycie bazy danych PostgreSQL. Należy zoptymalizować zapytania do bazy
danych.
- [x] Kod powinien być zgodny z PEP8.
- [ ] Dokumentacja API.
- [ ] Dokumentacja kodu źródłowego
- [ ] README.md z instrukcjami dotyczącymi instalacji, konfiguracji i uruchomienia
aplikacji.

### Dodatkowe informacje

- [x] Projekt powinien być dostępny w publicznym repozytorium na platformie
GitHub lub GitLab.
- [ ] Mile widziane użycie dobrych praktyk programistycznych, testy jednostkowe i
konfiguracja dockerowa/k8s.
- [x] Oceniane będą: czystość kodu, struktura projektu, stosowanie się do zasad
SOLID oraz efektywność rozwiązań.
- [x] Dobrym dodatkiem będzie korzystanie z wersji kontroli źródła Git, zgodnie z
zasadami (oceniane będą między innymi: nazwy i częstotliwość commitów).
- [x] Dodanie narzędzi deweloperskich np. przez Django Admin będzie
zdecydowanie dobrym dodatkiem.
- [x] Struktura projektu powinna być czytelna i umożliwiać łatwe poszerzanie
funkcjonalności.
