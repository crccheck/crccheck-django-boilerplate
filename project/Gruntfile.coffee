module.exports = (grunt) ->
  grunt.initConfig
    pkg: grunt.file.readJSON('package.json')
    sass:
      options:
        sourceMap: true
      dist:
        files:
          '{{ project_name }}/static/app.css': '{{ project_name }}/static_src/sass/app.sass'
    autoprefixer:
      options:
        browsers: ['last 2 versions']
        diff: true
        map: true
        single_file:
          src: '{{ project_name }}/static/app.css'
          # overwrite original
          dest: '{{ project_name }}/static/app.css'
    jshint:
      all: [
        '{{ project_name }}/static/js_src/**/*.js'
      ]
    browserify:
      app:
        files:
          '{{ project_name }}/static/app.js': '{{ project_name }}/static_src/app.js'
    uglify:
      app:
        files:
          '{{ project_name }}/static/app.min.js': ['{{ project_name }}/static/app.js']
    watch:
      # use live reload if the browser has it
      # if you don't have it you can get it here:
      # http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-
      options:
        livereload: true
      sass:
        files: ['{{ project_name }}/static_src/sass/**/*.sass']
        tasks: ['sass', 'autoprefixer']
        options:
          livereload: false
          # spawn has to be on or else the css watch won't catch changes
          spawn: true
      css:
        files: ['{{ project_name }}/static/*.css']
        options:
          spawn: false
      scripts:
        files: ['{{ project_name }}/static_src/**/*.js']
        tasks: ['browserify', 'uglify']
        options:
          spawn: false

  grunt.loadNpmTasks 'grunt-sass'
  grunt.loadNpmTasks 'grunt-autoprefixer'
  grunt.loadNpmTasks 'grunt-contrib-jshint'
  grunt.loadNpmTasks 'grunt-browserify'
  grunt.loadNpmTasks 'grunt-contrib-uglify'
  grunt.loadNpmTasks 'grunt-contrib-watch'

  # build the assets needed
  grunt.registerTask('build', ['sass', 'autoprefixer', 'browserify', 'uglify'])
  # build the assets with sanity checks
  grunt.registerTask('default', ['sass', 'autoprefixer', 'jshint', 'browserify', 'uglify'])
  # build assets and automatically re-build when a file changes
  grunt.registerTask('dev', ['build', 'watch'])
