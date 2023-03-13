#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a Python object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
    int i, size;
    PyListObject *list;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %d\n", size);

    list = (PyListObject *)p;
    printf("[*] Allocated = %d\n", (int)list->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}
