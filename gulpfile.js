/**
 * @fileoverview Gulpfile to compile SCSS to CSS.
 */

'use strict';

const path = require('path');

const gulp = require('gulp');
const importOnce = require('node-sass-import-once');
const rename = require('gulp-rename');
const scss = require('gulp-sass');

/**
 * This object contains options used by tasks. For example, source and
 * destination files, as well as configuration for plugins used in the
 * pipeline.
 *
 * Keys are task names, while values are objects, whose keys and values are
 * task-dependent. However, src and dest keys are generally expected.
 * Furthermore, a "watch" key can be defined, holding the source files for the
 * watcher version of the task.
 *
 * @summary Contains options for every task.
 *
 * @type Object
 */
const opts = {
    scss: {
        // Source and destination files
        src: './scss/templates/*.scss',
        dest: `${ __dirname }/static/css`,

        // Scss compilation options
        scss: {
            importer: importOnce,
            importOnce: {
                index: true,
                css: false,
                bower: false
            },

            includePaths: [
                ['foundation-sites', 'scss'],
                ['sassdash', 'scss']
            ].map(libPath => path.join(__dirname, 'node_modules', ...libPath))
        },

        // Options to rename files in the task pipeline
        rename: {
            dirname: ''
        },

        // SCSS watcher sources
        watch: './scss'
    }
};

/**
 * @summary Compiles SCSS files to CSS.
 */
gulp.task('scss', () =>
    gulp.src(opts.scss.src)
        .pipe(scss(opts.scss.scss).on('error', scss.logError))
        .pipe(rename(opts.scss.rename))
        .pipe(gulp.dest(opts.scss.dest))
);

/**
 * @summary Compiles SCSS to CSS when started and on SCSS changes.
 */
gulp.task('watch-scss', gulp.parallel(
        'scss',
        () => gulp.watch(opts.scss.watch, gulp.task('scss')))
);

/**
 * @summary Default task is aliased to watch.
 */
gulp.task('default', gulp.task('watch-scss'));


