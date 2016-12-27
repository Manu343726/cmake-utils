from conans import ConanFile, CMake

class ConanCMakeTest(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = 'cmake-utils/0.0.0@Manu343726/testing', 'clang/3.8.0@smspillaz/stable'
    generators = 'cmake'

    def test(self):
        cmake = CMake(self.settings)
        self.run('cmake {} {}'.format(self.conanfile_directory, cmake.command_line))
        self.run('cmake --build . {}'.format(cmake.build_config))
