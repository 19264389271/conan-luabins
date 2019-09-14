from conans import ConanFile, CMake, tools
import os
from shutil import copy


class LuabinsConan(ConanFile):
    name = "luabins"
    version = "0.3"
    description = "Allows to save tuples of primitive Lua types into binary chunks and to load saved data back."
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "luabins", "lua")
    url = "https://github.com/19264389271/conan-luabins"
    homepage = "https://github.com/agladysh/luabins"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    exports = ["LICENSE.md"]      # Packages the license for the conanfile.py
    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    requires = (
        "OpenSSL/1.0.2s@conan/stable",
        "zlib/1.2.11@conan/stable",
        "luajit/2.0.5@charliejiang/stable"
    )

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        source_url = "https://github.com/agladysh/luabins"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256="701f68b988fcd1b5cb874dfefc6df84830f6f2b801339c273395ab3ad9de79cb")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        copy("conanbuildinfo.cmake", os.path.join(self._source_subfolder, "conanbuildinfo.cmake"))
        copy("CMakeLists.txt", os.path.join(self._source_subfolder, "CMakeLists.txt"))
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder,source_folder = self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder,source_folder = self._source_subfolder)
        cmake.install()
        # If the CMakeLists.txt has a proper install method, the steps below may be redundant
        # If so, you can just remove the lines below
        # include_folder = os.path.join(self._source_subfolder, "include")
        # self.copy(pattern="*", dst="include", src=include_folder)
        # self.copy(pattern="*.dll", dst="bin", keep_path=False)
        # self.copy(pattern="*.lib", dst="lib", keep_path=False)
        # self.copy(pattern="*.a", dst="lib", keep_path=False)
        # self.copy(pattern="*.so*", dst="lib", keep_path=False)
        # self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
