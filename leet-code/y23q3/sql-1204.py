s = '''
    with base_table as (
        select 
            *, rank() 
            over(
                order by running_total desc
            ) as ranking
        from (
            select *, 
            sum(weight) 
            over(order by turn) 
            as running_total
        from queue) A
        where running_total <= 1000)
        select person_name
        from base_table
        where ranking = 1
'''
