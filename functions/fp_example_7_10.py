# Fluent Python ex.7.10 (p.240-241)
# Positional and Keyword Function Parameters
def tag(name, *content, class_=None, **attrs):
    """Generate one or more HMTML tags"""
    if class_ is not None:
        attrs["class"] = class_

    attr_pairs = (f" {attr}='{value}'" for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)

    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)
        return "\n".join(elements)
    return f"<{name}{attr_str} />"


print(tag("br"))

# Any number of arguments after the first are captured by `*content` as a `tuple`:
print(tag("p", "Hello!"))
print(tag("p", "Hello", "world!"))

# Keyword arguments not explicitly named in the tag signature are captured by
# `**attrs` as a `dict`:
print(tag("p", "hello", id=33))

# The `class_` parameter can only be passed as a keyword argument:
print(tag("p", "hello", "world", class_="sidebar"))

# Prefixing the my_tag dict with ** passes all its items as separate arguments,
# which are then bound to the named parameters, with the remaining caught by
# **attrs. In this case we can have a 'class' key in the arguments dict, because
# it is a string, and does not clash with the class reserved word:
my_tag = {
    "name": "img",
    "title": "Sunset Boulevard",
    "src": "sunset.jpg",
    "class": "framed",
}
print(tag(**my_tag))
