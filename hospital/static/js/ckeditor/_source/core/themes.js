/*
Copyright (c) 2003-2012, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

/**
 * @fileOverview Defines the {@link CKEDITOR.themes} object, which is used to
 *		manage themes registrations and loading.
 */

/**
 * Manages themes registrations and loading.
 * @namespace
 * @augments CKEDITOR.resourceManager
 * @example
 */
CKEDITOR.themes = new CKEDITOR.resourceManager(
	'_source/'+		// @Packager.RemoveLine
	'themes/', 'theme' );
