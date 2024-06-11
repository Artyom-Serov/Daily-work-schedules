document.addEventListener('DOMContentLoaded', function() {
    const addWorkButton = document.querySelector ('.add-work');
    const formsetPrefix = '{{ formset.prefix }}';
    let formIndex = {{ formset.total_form_count }};

    addWorkButton.addEventListener('click', function() {
        const newForm = document.createElement('div');
        newForm.innerHTML =
            <li class="work-form">
                ${document.querySelector('.work-form').innerHTML.replace(
                    /form-\d+/g, 'form-${formIndex}'
                )}
            </li>;
        document.querySelector('ul').appendChild(newForm);
        formIndex++;
    });

    document.querySelectorAll('.add-resource').forEach(button => {
        button.addEventListener('click', function() {
            const resourceFormset = button.previousElementSibLing;
            let resourceFormIndex = resourceFormset.children.length - 1;
            const newResourceForm = document.createElement('div');
            newResourceForm.innerHTML =
                <ul>
                    ${resourceFormset.children[1].innerHTML.replace(
                        /form-\d+-resource-\d+/g, 'form-${resourceFormIndex}'
                    )}
                </ul>
            resourceFormset.appendChild(newResourceForm);
        });
    });
});