#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A pointer to PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    int size, alloc, i;
    PyObject *obj;

    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);
        /*
        these 2 line can be repleced with

        PyListObject obj = (PyListObject *)p
        printf("%s\n", Py_TYPE(obj->obj_item[i])->tp_name);
          */
        obj = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}
