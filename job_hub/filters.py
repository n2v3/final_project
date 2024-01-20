import django_filters

from .models import Vacancy


class VacancyFilter(django_filters.FilterSet):
    # SALARY_CHOICES = [
    #     (1, 'Less than 500'),
    #     (2, '500 - 1000'),
    #     (3, '1000 - 2000'),
    #     (4, '2000 - 3500'),
    #     (5, '3500 - 5000'),
    #     (6, 'Above 5000'),
    # ]

    CATEGORY_CHOICES = [
        (1, 'Information Technology'),
        (2, 'Healthcare'),
        (3, 'Finance'),
        (4, 'Education'),
        (5, 'Marketing'),
        (6, 'Engineering'),
        (7, 'Sales'),
        (8, 'Customer Service'),
        (9, 'Retail'),
        (10, 'Human Resources'),
    ]

    job_title = django_filters.CharFilter(lookup_expr='iexact', label='Job Title')
    requirements = django_filters.CharFilter(lookup_expr='icontains', label='Requirements')


    company_name = django_filters.CharFilter(
        field_name='company_profile__company_name',
        lookup_expr='iexact',
        label='Company Name'
    )

    # salary = django_filters.ChoiceFilter(
    #     field_name='salary',
    #     choices=SALARY_CHOICES,
    #     label='Salary Range',
    #     lookup_expr='exact',  # Use 'exact' to match the selected choice exactly
    # )

    category = django_filters.ChoiceFilter(
        field_name='category',
        choices=CATEGORY_CHOICES,
        label='Category',
        lookup_expr='exact',  # Use 'exact' to match the selected choice exactly
    )

    # filter by q
    # q = django_filters.CharFilter(method='filter_by_q', label='Search')
    #
    # def filter_by_q(self, queryset, name, value):
    #     return queryset.filter(description__icontains=value) | queryset.filter(requirements__icontains=value) | queryset.filter(job_title__icontains=value)

