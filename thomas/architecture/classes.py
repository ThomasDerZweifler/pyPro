import os

package = "plugin/"
cls = "Plugin"

for dirpath, dirnames, filenames in os.walk("plugin/"):
    if(dirpath == package):

        for filename in filenames:
            module = __import__("plugin." + filename[0:-3], fromlist=[''])
            print( "name of module: " + module.__name__)

            #print(dir(module))

            c = getattr(module,cls)
            print("id: " + c.identifier())
            if(c.__name__ == cls):
                print("version: " + c().version())

