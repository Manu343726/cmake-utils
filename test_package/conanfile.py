from conans import ConanFile, CMake

class ConanCMakeTest(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = 'cmake-utils/0.0.0@Manu343726/testing'
    generators = 'cmake'

    def test(self):
        self.run('cmake {}'.format(self.conanfile_directory))
