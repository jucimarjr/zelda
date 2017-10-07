from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

class FlashErrorsNegocio:
    def flash_errors(form):
        for field, errors in form.errors.items():
            for error in errors:
                flash("%s" %(
                    error))