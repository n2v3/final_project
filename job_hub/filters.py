import django_filters


class VacancyFilter(django_filters.FilterSet):

    CATEGORY_CHOICES = [
        (1, "Information Technology"),
        (2, "Healthcare"),
        (3, "Finance"),
        (4, "Education"),
        (5, "Marketing"),
        (6, "Engineering"),
        (7, "Sales"),
        (8, "Customer Service"),
        (9, "Retail"),
        (10, "Human Resources"),
    ]

    job_title = django_filters.CharFilter(
        lookup_expr="iexact", label="Job Title"
    )
    requirements = django_filters.CharFilter(
        lookup_expr="icontains", label="Requirements"
    )

    company_name = django_filters.CharFilter(
        field_name="company_profile__company_name",
        lookup_expr="iexact",
        label="Company Name",
    )

    category = django_filters.ChoiceFilter(
        field_name="category",
        choices=CATEGORY_CHOICES,
        label="Category",
        lookup_expr="exact",
    )

    # filter by q
    # q = django_filters.CharFilter(method='filter_by_q', label='Search')
    #
    # def filter_by_q(self, queryset, name, value):
    #     return (
    #             queryset.filter(description__icontains=value) |
    #             queryset.filter(requirements__icontains=value) |
    #             queryset.filter(job_title__icontains=value)
    #     )
