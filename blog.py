import web
import model

urls = ('/', 'Index',
        '/view/(\d+)', 'View',
        '/new','New',
        '/delete/(\d+)','Delete',
        '/edit/(\d+)','Edit',
)

t_global = {
    'datestr':web.datestr
}

render = web.template.render('templates', base='base', globals=t_global)

class Index:
    def GET(self):
        '''show page'''
        posts = model.get_posts()
        return render.index(posts)

class View:
    def GET(self, id):
        '''view single post'''
        post = model.get_post(int(id))
        return render.view(post)

class New:
    form = web.form.Form(
        web.form.Textbox('title',web.form.notnull,size=30,description='post title'),
        web.form.Textarea('content',web.form.notnull,rows=30,cols=80,description='post content'),
        web.form.Button('Post entry'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')

class Delete:
    def POST(self,id):
        model.del_post(id)
        raise web.seeother('/')

class Edit:
    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)

    def POST(self, id):
        form = New.form()
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()