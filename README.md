# GIT


# Tworzenie repo
git init
Opis: Inicjalizuje nowe repozytorium Git.
Przykład: git init


# Klonowanie repo
git clone [url]
Opis: Klonuje istniejące repozytorium z podanego URL.
Przykład: git clone https://github.com/przyklad/repo.git

git clone [url] [katalog] 

git clone --branch [branch-name] [url]

git clone --depth 1 [url] (historia ostatniego commitu - ostatni commit)

git clone --mirror [url]


# Dodawanie do stagingu
git add [file] (dodaj konkretny plik)
git add [directory] (dodaj ścieżkę)

git add . / git add -A (dodaj wszystko)

git add -u (dodaj wszystkie pliki zmodyfikowane[bez nowych plików])

git add --ignore-removal (ignoruje pliki usunięte)

git add [file1] [file2]

git add ".py" (wszystkie pliki typu .py)


# Commitowanie zmian
git commit -m "[commit message]" 

git commit -a -m "[commit message]" / git commit -am "[commit message]"

git commit --amend -m "[change last commit message]"

git commit --amend --no-edit

git commit --allow-empty -m "Pusty commit"

git commit -m "Tytuł commita" -m "Dalszy opis zmian" (2 komentarze linia pod linią)


# Status zmian w repozytorium
git status

git status -s

git status -b

git status --ignored (uwzględnia ignorowane pliki)

git status --show-stash

git status -u (pokazuje też niedodane pliki)


# Ściąganie zmian
git pull / git pull origin

git pull origin dev

git pull --verbose
git pull --dry-run

git pull --no-commit origin feature (pobierze zmiany, ale nie w formie commitu)


# Git remote
git remote

git remote -v

git remote add [nazwa] [url]

git remote rename [old-name] [new-name]

git remote rm [shortname] (usuwanie remote)

git remote show [shortname] (pokazuje informacje o danym repozytorium)

git remote update

git remote set-url [shortname] [new-url]

git remote set-head [shortname] -a
git pull. git push


# Git config
git config --global user.name "[name]"
git config --global user.email "[email address]"

git config --global core.editor "[editor]"

git config --list

git config [key]
    ^^^^^
git config user.mail

git config --global alias.[alias-name] '[command]'
git config --global alias.st 'status'

/n/r
git config --global core.autocrlf [true|false|input]

git config --global core.ignorecase [true|false]

git config --global merge.tool [tool]

git config --global diff.tool [tool]

git config --global core.filemode [true|false]


# Branche
git branch (wyświetlenie wszystkich branchy)

git branch [branch-name] (utworzenie nowego brancha)

git branch -d [branch-name] (usunięcie brancha)

git branch -D [branch-name] (wymusza usunięcie gałęzi)

git branch -m [old-name] [new-name] (zmienia nazwę brancha)

git branch -r (wyświetlenie zdalnych branchy)

git branch --show-current

git branch -v

git branch --merged

git branch --no-merged [branch]

git branch --contains [commit] (wyświetlenie brancha zawierającego dany commit)

git branch -vv

git branch --sort=[key]

git branch --sort=committerdate

git branch [branch-namme] [start-point]

git branch --copy [feature-old] [feature-new] (skopiowanie brancha)

git branch --edit-description [branch-name]

git branch --list [pattern]