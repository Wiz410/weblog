class BootstrapFormMixin():
    """Вспомогательная Форма.
    - Переопределяет `__init__` для добавлен классов `bootstrap` к полям формы.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })