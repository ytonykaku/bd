import psycopg2
import os
import sql


def main():
    database = sql.CampeonatoBrasileiro()

    sql_files = ["sql\\estados_do_brasil\\table.sql",
                 "sql\\jogo\\table.sql",
                 "sql\\team\\table.sql",
                 "sql\\jogador\\table.sql",
                 "sql\\stats_jogador\\table.sql",
                 "sql\\substituicoes\\table.sql",
                 "sql\\stats_time\\table.sql",
                 "sql\\faltas\\table.sql",
                 "sql\\gols\\table.sql",
                 "sql\\stats_jogo\\table.sql"
                 ]

    sql_inserts = ["sql\\estados_do_brasil\\insert.sql",
                   "sql\\jogo\\insert.sql",
                   "sql\\team\\insert.sql",
                   "sql\\jogador\\insert.sql",
                   "sql\\stats_jogador\\insert.sql",
                   "sql\\substituicoes\\insert.sql",
                   "sql\\stats_time\\insert.sql",
                   "sql\\faltas\\insert.sql",
                   "sql\\gols\\insert.sql",
                   "sql\\stats_jogo\\insert.sql"
                   ]

    sql_views = ["sql\\views\\view1.sql",
                 "sql\\views\\view2.sql",
                 "sql\\views\\view3.sql",
                 "sql\\views\\view4.sql",
                 "sql\\views\\view5.sql",
                 "sql\\views\\view6.sql"
                 ]

    database.execute_sql_files(sql_files)
    database.execute_sql_files(sql_inserts)
    database.execute_sql_files(sql_views)

    database.close_connection()


if __name__ == "__main__":
    main()
