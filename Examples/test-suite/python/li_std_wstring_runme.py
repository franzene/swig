import li_std_wstring
import sys

x = u"h"

if li_std_wstring.test_wcvalue(x) != x:
    print li_std_wstring.test_wcvalue(x)
    raise RuntimeError("bad string mapping")

x = u"hello"
if li_std_wstring.test_ccvalue(x) != x:
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_cvalue(x) != x:
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_wchar_overload(x) != x:
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_wchar_overload("not unicode") != "not unicode":
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_value(x) != x:
    print x, li_std_wstring.test_value(x)
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_const_reference(x) != x:
    raise RuntimeError("bad string mapping")


s = li_std_wstring.wstring(u"he")
s = s + u"llo"

if s != x:
    print s, x
    raise RuntimeError("bad string mapping")

if s[1:4] != x[1:4]:
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_value(s) != x:
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_const_reference(s) != x:
    raise RuntimeError("bad string mapping")

a = li_std_wstring.A(s)

if li_std_wstring.test_value(a) != x:
    raise RuntimeError("bad string mapping")

if li_std_wstring.test_const_reference(a) != x:
    raise RuntimeError("bad string mapping")

b = li_std_wstring.wstring(" world")

if a + b != "hello world":
    raise RuntimeError("bad string mapping")

if a + " world" != "hello world":
    raise RuntimeError("bad string mapping")

# This is expected to fail if -builtin is used
# Reverse operators not supported in builtin types
if not li_std_wstring.is_python_builtin():
    if "hello" + b != "hello world":
        raise RuntimeError("bad string mapping")

    c = "hello" + b
    if c.find_last_of("l") != 9:
        raise RuntimeError("bad string mapping")

s = "hello world"

b = li_std_wstring.B("hi")

b.name = li_std_wstring.wstring(u"hello")
if b.name != "hello":
    raise RuntimeError("bad string mapping")


b.a = li_std_wstring.A("hello")
if b.a != u"hello":
    raise RuntimeError("bad string mapping")

# Byte strings only converted in Python 2
if sys.version_info[0:2] < (3, 0):
    x = b"hello there"
    if li_std_wstring.test_value(x) != x:
        raise RuntimeError("bad string mapping")

# Invalid utf-8 in a byte string fails in all versions
x = b"h\xe9llo"
try:
    li_std_wstring.test_value(x)
    raise RuntimeError("TypeError not thrown")
except TypeError:
    pass

# Check surrogateescape
if sys.version_info[0:2] > (3, 1):
    x = u"h\udce9llo"  # surrogate escaped representation of C char*: "h\xe9llo"
    if li_std_wstring.non_utf8_c_str() != x:
        raise RuntimeError("surrogateescape not working")
    if li_std_wstring.size_wstring(x) != 5 and len(x) != 5:
        raise RuntimeError("Unexpected length")
