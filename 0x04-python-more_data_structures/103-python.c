#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A PyObject bytes object
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    unsigned int i, size;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    printf("  size: %d\n", size);
    printf("  trying string: %s\n", bytes->ob_sval);

    printf("  first %d bytes:", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02x", bytes->ob_sval[i]);

    printf("\n");
}


/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A PyObject list object
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    PyObject *item;
    unsigned int i, size;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int)list->allocated);

    for (i = 0; i < size; i++)
    {
        item = list->ob_item[i];
        printf("Element %d: ", i);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyList_Check(item))
            print_python_list(item);
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("%s\n", item->ob_type->tp_name);
    }
}
