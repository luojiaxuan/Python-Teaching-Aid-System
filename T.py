# -*- coding: UTF-8 -*-
from random import sample
from os import listdir, rename
from os.path import splitext
import sys
sys.path.append('../')
sys.path.append('./')
from python.Graph import collect as collection

###### 读取作业

path = './files'
# listdir方法返回文件夹中的文件和文件夹列表
dir = listdir(path)
print(dir)
#dir = listdir(glob.glob(r"./files/"))

for file in dir:
    # 如果命名不规范，则跳过
    if not file.endswith('.py'):
        continue
    # 改名，前面加字母，防止数字开头的文件名无法作为模块导入
    rename('./files/' + file, './files/' + 'a' + file)
    # 手动更改python程序中的文件名
    file = 'a' + splitext(file)[0]
    # 导入试卷并判断是否成功
    try:
        print('from ' + 'files.' + file + ' import *')
        exec('from ' + 'files.' + file + ' import *')
    except Exception as e:
        print(e)
        print("导入失败！")
        continue
    # 导入成功，开始判卷
    print('=' * 30 + '\n正在披阅试卷:' + file[1:])
    total = 0
    # 学号
    id = file[1:]

    try:
        # 回文判断
        '''if one('deed') and not one('beed'):
            print(one)
            print('第一题ok')
            total += 20'''
        print(getReward(2000))
    except Exception as e:
        print('sss')

    except StopIteration as e:
        errName = 'StopIteration'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except ArithmeticError as e:
        errName = 'ArithmeticError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except AssertionError as e:
        errName = 'AssertionError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except AttributeError as e:
        errName = 'AttributeError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except BufferError as e:
        errName = 'BufferError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except EOFError as e:
        errName = 'EOFError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except ImportError as e:
        errName = 'ImportError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except LookupError as e:
        errName = 'LookupError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except MemoryError as e:
        errName = 'MemoryError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except NameError as e:
        errName = 'NameError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except OSError as e:
        errName = 'OSError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except ReferenceError as e:
        errName = 'ReferenceError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except RuntimeError as e:
        errName = 'RuntimeError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except SyntaxError as e:
        errName = 'SyntaxError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except TypeError as e:
        errName = 'TypeError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except ValueError as e:
        errName = 'ValueError'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)
    except Warning as e:
        errName = 'Warning'
        err = str(e)
        name = str(id)
        print(err)
        #collection.collectStudent(name, err, errName)

    try:
        print(getPrimeNumber(200,300))


    except StopIteration as e:

        errName = 'StopIteration'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except ArithmeticError as e:

        errName = 'ArithmeticError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except AssertionError as e:

        errName = 'AssertionError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except AttributeError as e:

        errName = 'AttributeError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except BufferError as e:

        errName = 'BufferError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except EOFError as e:

        errName = 'EOFError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except ImportError as e:

        errName = 'ImportError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except LookupError as e:

        errName = 'LookupError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except MemoryError as e:

        errName = 'MemoryError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except NameError as e:

        errName = 'NameError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except OSError as e:

        errName = 'OSError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except ReferenceError as e:

        errName = 'ReferenceError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except RuntimeError as e:

        errName = 'RuntimeError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except SyntaxError as e:

        errName = 'SyntaxError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except TypeError as e:

        errName = 'TypeError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except ValueError as e:

        errName = 'ValueError'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    except Warning as e:

        errName = 'Warning'

        err = str(e)

        name = str(id)

        print(err)

        #collection.collectStudent(name, err, errName)

    #rename('./python/files/' + file + '.py', './python/files/' + file[1:] + '.py')
    print(file[1:], total)

#collection.collectClass()
