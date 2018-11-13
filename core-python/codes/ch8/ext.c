#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#include "Python.h"


int fac(int n) {
  if(n < 2)
    return 1;

  return n * fac(n-1);
}


char *reverse(char *s) {
  register char t,
           *p = s,
           *q = (s + (strlen(s) - 1));

  while(p < q) {
    t = *p;
    *p++ = *q;
    *q-- = t;
  }

  return s;
}

static PyObject *ext_fac(PyObject *self, PyObject *args) {
  int num;
  if(!PyArg_ParseTuple(args, "i", &num))
    return NULL;

  return (PyObject*) Py_BuildValue("i", fac(num));
}


static PyObject *ext_doppel(PyObject *self, PyObject *args) {
  char *orig_str;
  char *dupe_str;
  PyObject *retval;

  if(!PyArg_ParseTuple(args, "s", &orig_str))
    return NULL;

  retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));
  free(dupe_str);
  return retval;
}

static PyMethodDef extMethods[] = {
  {"fac", ext_fac, METH_VARARGS},
  {"doppel", ext_doppel, METH_VARARGS},
  {NULL, NULL}
};


void initext() {
  Py_InitModule("ext", extMethods);
}
