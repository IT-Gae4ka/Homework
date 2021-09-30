# Run the module modules/mod_a.py. Check its result. Explain why does this happen. Try to change x to a list [1,2,3]. Explain the result. Try to change import to from x import * where x - module names. Explain the result.

# Запустите модуль modules / mod_a.py. Проверьте его результат. Объясните, почему это происходит. Попробуйте заменить x на список [1,2,3]. Объясните результат. Попробуйте изменить import на from x import *, где x - имена модулей. Объясните результат.

1. result: 5
reason: mod_c.x was imported from mod_b

2. result: 5
reason: mod_c is imported, mod_c code is run and variable x = [1,2,3] is created.
		mod_b is imported, the mod_b code is run, which in turn runs the mod_c code again and accesses x = [1,2,3], and then overwrites it in 5
		the last line of the mod_a prints the variable already changed to 5 from mod_c

3.result: 5
	the same result, because import mod_b/mod_c is almost the same as from mod_b/mod_c import * (all)
	