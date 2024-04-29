import sys
import types


def package_imports(globals):
    """
    Yields a tuple of (package_name, version) for all imported packages in the given global namespace.

    This function iterates over the objects in the global namespace and identifies the imported packages,
    including those imported using the 'import' statement and 'from package import module' syntax.

    Args:
        globals (dict): The global namespace dictionary containing all variables and objects.

    Yields:
        tuple: A tuple containing the package name (str) and version (str or None) for each imported package.

    Notes:
        - For packages imported using the 'import' statement, the package name and version are retrieved
          from the module object's '__name__' and '__version__' (or 'version') attributes, respectively.
        - For objects imported using 'from package import module' syntax, the package name is derived from
          the object's '__module__' attribute, and the version is retrieved from the top-level package
          module's '__version__' attribute (if available).
        - If the package does not have a '__version__' or 'version' attribute, the version is set to None.
        - The function assumes that the top-level package has a '__version__' attribute. If the package
          doesn't have a '__version__' attribute, the code will yield None for the version.
    """
    for name, obj in globals.items():
        if isinstance(obj, types.ModuleType):
            if hasattr(obj, '__version__'):
                version = obj.__version__
            elif hasattr(obj, 'version'):
                version = obj.version
            else:
                version = None
            if hasattr(obj, '__name__'):
                package_name = obj.__name__
            else:
                package_name = name
            yield (package_name, version)
        elif isinstance(obj, types.ModuleType.__base__):
            # Handle cases where modules are imported using 'from package import module'
            if hasattr(obj, '__module__'):
                package_name = obj.__module__.split('.')[0]  # Get the top-level package name
                package_module = sys.modules.get(package_name)
                if package_module:
                    version = getattr(package_module, '__version__', None)
                else:
                    version = None
                yield (obj.__module__, version)