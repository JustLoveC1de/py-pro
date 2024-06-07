# my first task
import os.path
import json
import time
class Levels: 
    LEVEL_START: int = 0
    LEVEL_DICT_GET: int = 1
    LEVEL_DICT_WRITE: int = 2
    LEVEL_END: int = 3
STANDART_VALUES: dict = {
    'лол': 'очень смешно',
    'кринж': 'что-то странное, стыдное',
    'рофл': 'шутка',
    'щищ': 'одобрение или восторг',
    'криповый': 'страшный, пугающий',
    'агриться': 'злиться'
}
CONFIG_NAME: str = 'dict.json'
def checkDict() -> bool:
    return os.path.exists(CONFIG_NAME)

# operations with conf
def createConf() -> None:
    with open(CONFIG_NAME, 'wt+') as conf:
        conf.write(json.dumps(STANDART_VALUES, ensure_ascii=False, indent=4))
        print("Создан файл!")

def writeConf(pair: tuple) -> None:
    currentContents: dict = getConf()
    if pair[0] in currentContents.keys():
        raise KeyError
    currentContents[pair[0]] = pair[1]
    with open(CONFIG_NAME, 'wt+') as conf:
        conf.write(json.dumps(currentContents,ensure_ascii=False,indent=4))


def getConf() -> dict:
    with open(CONFIG_NAME, 'rt') as conf:
        return json.loads(conf.read())

# main logic
def main() -> None:
    print('> Приветствую вас в программе «Словарь нового поколения»!')
    if not checkDict(): # Создание словаря
        createConf()
    level = Levels.LEVEL_START
    def level_start() -> None:
        cmd = input('Пожалуйста, введите одну из трёх команд: «выход», «определение», «запись» | ').casefold()
        nonlocal level
        match cmd:
            case 'выход':
                print('> Надеюсь, данная программа была полезной!')
                level = Levels.LEVEL_END
            case 'определение':
                print('> Переходим в режим получения определения слова...')
                level = Levels.LEVEL_DICT_GET
            case 'запись':
                print('> Переходим в режим записи новых слов...')
                level = Levels.LEVEL_DICT_WRITE
            case _:
                print('> Такой команды не существует!')
    def level_dict_get() -> None:
        cmd = input('Пожалуйста, введите одну из двух команд: «назад», «получить <слово>» | ').casefold().split(maxsplit=1)
        nonlocal level
        match cmd[0]:
            case 'назад':
                print('> Возвращаемся в начало...')
                level = Levels.LEVEL_START
            case 'получить':
                try:
                    word = cmd[1]
                    print(f"| Определение слова «{word}»: «{getConf()[word]}»")
                except IndexError:
                    print('> Вами не было предоставлено аргументов!')
                except KeyError:
                    print('> Данное слово не было определено!')
            case _:
                print('> Такой команды не существует!')
    def level_dict_write() -> None:
        cmd = input('Пожалуйста, введите одну из двух команд: «назад», «записать <слово> <определение>» | ').casefold().split(maxsplit=2)
        nonlocal level
        match cmd[0]:
            case 'назад':
                print('> Возвращаемся в начало...')
                level = Levels.LEVEL_START
            case 'записать':
                try:
                    args = cmd[1], cmd[2]
                    writeConf(args)
                    print(f"| Теперь определение слова «{args[0]}» записано как: «{args[1]}»")
                except IndexError:
                    print('> Вами не были предоставлены все аргументы!')
                except KeyError:
                    print('> Данное слово уже было определено!')
            case _:
                print('> Такой команды не существует!')
    while True: # Выполнение команд в зависимости от "уровня" пользователя
        match level:
            case Levels.LEVEL_START:
                level_start()
            case Levels.LEVEL_DICT_GET:
                level_dict_get()
            case Levels.LEVEL_DICT_WRITE:
                level_dict_write()
            case Levels.LEVEL_END:
                break
            case _:
                raise NotImplementedError
    


if __name__ == '__main__':
    main()
