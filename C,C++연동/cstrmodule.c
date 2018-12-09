#include <python3.6/Python.h>

static PyObject *
cstr_strlen(PyObject *self, PyObject *args)         //strlen함수 정의
{
	const char* str = NULL;

	int len = 0;

	if (!PyArg_ParseTuple(args, "s", &str)) {
		return NULL;
	}

	len = strlen(str);

	return Py_BuildValue("i", len);
}

/*static PyObject *
cstr_division(PyObject *self, PyObject *args)      //division함수 정의
{
	int quotient = 0;
	int dividend, divisor = 0;

	if (!PyArg_ParseTuple(args, "ii", &dividend, &divisor)) {
		return NULL;
	}

	if (divisor) {
		quotient = dividend / divisor;
	}
	else {                                 //ZeroDivision에러 예외처리
		PyErr_SetString(PyExc_ZeroDivisionError, "divisor must not be zero");
		return NULL;
	}

	return Py_BuildValue("i", quotient);
}*/

static PyMethodDef CstrMethods[] = {            //함수의 속성 정의, __dict__속성에 저장
   {"strlen", cstr_strlen, METH_VARARGS,         //파이썬에서 함수이름, 함수포인터, 자료형결정 상수, 함수에 대한 설명
	"count a string length."},
   /*{"divison", cstr_division, METH_VARARGS,
	"division function \n return quotient, quotient is dividend / divisor"},*/
   {NULL, NULL, 0, NULL}                     //배열의 끝
};

static struct PyModuleDef cstrmodule = {         //생성할 모듈의 정보가 담긴 구조체
   PyModuleDef_HEAD_INIT,
   "cstr",									 //모듈이름
   "It is test module.",                     //모듈 설명, 모듈의 __doc__에 저장
   -1, CstrMethods
};

PyMODINIT_FUNC
PyInit_cstr()                              //모듈 초기화
{
	return PyModule_Create(&cstrmodule);
}