from conans import ConanFile

class CMakeUtils(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    name = 'cmake-utils'
    url  = 'https://github.com/Manu343726/cmake-utils'
    version = '0.0.0'
    exports = '*.cmake'

    def package(self):
        self.copy('*.cmake')
