#include <python3.6/Python.h>

static PyObject *
cstr_strlen(PyObject *self, PyObject *args)         //strlen�Լ� ����
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
cstr_division(PyObject *self, PyObject *args)      //division�Լ� ����
{
	int quotient = 0;
	int dividend, divisor = 0;

	if (!PyArg_ParseTuple(args, "ii", &dividend, &divisor)) {
		return NULL;
	}

	if (divisor) {
		quotient = dividend / divisor;
	}
	else {                                 //ZeroDivision���� ����ó��
		PyErr_SetString(PyExc_ZeroDivisionError, "divisor must not be zero");
		return NULL;
	}

	return Py_BuildValue("i", quotient);
}*/

static PyMethodDef CstrMethods[] = {            //�Լ��� �Ӽ� ����, __dict__�Ӽ��� ����
   {"strlen", cstr_strlen, METH_VARARGS,         //���̽㿡�� �Լ��̸�, �Լ�������, �ڷ������� ���, �Լ��� ���� ����
	"count a string length."},
   /*{"divison", cstr_division, METH_VARARGS,
	"division function \n return quotient, quotient is dividend / divisor"},*/
   {NULL, NULL, 0, NULL}                     //�迭�� ��
};

static struct PyModuleDef cstrmodule = {         //������ ����� ������ ��� ����ü
   PyModuleDef_HEAD_INIT,
   "cstr",									 //����̸�
   "It is test module.",                     //��� ����, ����� __doc__�� ����
   -1, CstrMethods
};

PyMODINIT_FUNC
PyInit_cstr()                              //��� �ʱ�ȭ
{
	return PyModule_Create(&cstrmodule);
}